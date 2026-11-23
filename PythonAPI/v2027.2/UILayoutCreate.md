**English** • [Deutsch](../../PythonAPI.de/v2027.2/UILayoutCreate.md) • [日本語](../../PythonAPI.ja/v2027.2/UILayoutCreate.md)

# UILayoutCreate — alerts, standard dialogs and layout dialogs

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The user interface classes: `Alerts` (message boxes, questions, warnings and errors), `StandardDialogs` (ready-made dialogs that edit one or two values or choose from a list) and `LayoutDialog` (any modal dialog, built control by control, with event handlers written in Python). The value types `DialogEvent` and `ListBrowserEvent` and the dialog enumerations belong to this group too.

Dialogs are modal: `Run()` returns when the user closes the dialog. Control values stay readable after `Run()`.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [DialogEvent](#dialogevent)
  - [ListBrowserEvent](#listbrowserevent)
  - [DialogSize](#dialogsize)
  - [Alerts](#alerts)
  - [TextPair](#textpair)
  - [StandardDialogs](#standarddialogs)
  - [LayoutDialog](#layoutdialog)
- [Enumerations](#enumerations)
  - [DialogResult](#dialogresult)
  - [AlertButton](#alertbutton)
  - [EditRealType](#editrealtype)
  - [StaticTextStyle](#statictextstyle)
  - [CheckState](#checkstate)
  - [DialogEventType](#dialogeventtype)
  - [ListBrowserControlType](#listbrowsercontroltype)
  - [ListBrowserDisplayType](#listbrowserdisplaytype)
  - [ListBrowserEventType](#listbrowsereventtype)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`DialogEvent`](#dialogevent) | class |  | One event delivered to a layout dialog handler. |
| [`ListBrowserEvent`](#listbrowserevent) | class |  | Detail of the last list browser event. |
| [`DialogSize`](#dialogsize) | class |  | Size of a dialog, in pixels. |
| [`Alerts`](#alerts) | class |  | Standard Vectorworks alerts: information, error and question alerts (static functions only). |
| [`TextPair`](#textpair) | class |  | Values entered in the two-text dialog. |
| [`StandardDialogs`](#standarddialogs) | class |  | Ready-made dialogs that edit one or two values or choose from a list (static functions only). |
| [`LayoutDialog`](#layoutdialog) | class |  | Modal layout manager dialog, built control by control in code. |
| [`DialogResult`](#dialogresult) | IntEnum |  | How a dialog or an alert was closed. |
| [`AlertButton`](#alertbutton) | IntEnum |  | Default button of a question alert. |
| [`EditRealType`](#editrealtype) | IntEnum |  | Kind of value shown by a real number edit field. |
| [`StaticTextStyle`](#statictextstyle) | IntEnum |  | Font style of a static text. |
| [`CheckState`](#checkstate) | IntEnum |  | State of a three-state check box, a list browser cell or a tree item check box. |
| [`DialogEventType`](#dialogeventtype) | IntEnum |  | Kind of a dialog event (see DialogEvent). |
| [`ListBrowserControlType`](#listbrowsercontroltype) | IntEnum |  | Behavior of a list browser column. |
| [`ListBrowserDisplayType`](#listbrowserdisplaytype) | IntEnum |  | What a list browser column shows. |
| [`ListBrowserEventType`](#listbrowsereventtype) | IntEnum |  | What happened in a list browser (see `LayoutDialog.GetListBrowserEvent`). |

## Classes

### DialogEvent

> **Full name:** `api.DialogEvent` · **Inherits:** `api.Object`

One event delivered to a layout dialog handler.

**Constructors**

| Constructor | Description |
|---|---|
| `DialogEvent()` | Default value (fields at their defaults). |
| `DialogEvent(fDialogID, fControlID, fEvent, fData, fIsNegative)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fDialogID` | `int` | Layout manager ID of the dialog. |
| `fControlID` | `int` | Control that caused a Control event; 1 for Ok, 2 for Cancel, 0 otherwise. |
| `fEvent` | `DialogEventType` | Kind of event. |
| `fData` | `int` | Control specific value (e.g. the new slider position, the chosen color as 0x00RRGGBB), or the message code for Other. |
| `fIsNegative` | `bool` | The layout manager reported the control event with a negative ID (secondary action, e.g. list browser double click). |

### ListBrowserEvent

> **Full name:** `api.ListBrowserEvent` · **Inherits:** `api.Object`

Detail of the last list browser event.

**Constructors**

| Constructor | Description |
|---|---|
| `ListBrowserEvent()` | Default value (fields at their defaults). |
| `ListBrowserEvent(fEvent, fRow, fColumn)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fEvent` | `ListBrowserEventType` | Kind of list browser event. |
| `fRow` | `int` | Row of the event (0-based). |
| `fColumn` | `int` | Column of the event (0-based). |

### DialogSize

> **Full name:** `api.DialogSize` · **Inherits:** `api.Object`

Size of a dialog, in pixels.

**Constructors**

| Constructor | Description |
|---|---|
| `DialogSize()` | Default value (fields at their defaults). |
| `DialogSize(fWidth, fHeight)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fWidth` | `int` | Width in pixels. |
| `fHeight` | `int` | Height in pixels. |

### Alerts

> **Full name:** `api.Alerts` · **Inherits:** `api.Object`

Standard Vectorworks alerts: information, error and question alerts (static functions only).

**Constructors**

Not instantiable from Python: use the static methods on the class (`api.Alerts.Method(...)`).

**Methods**

| Method | Description |
|---|---|
| `Inform(text: str, advice: str = '', isMinor: bool = False, category: str = '', item: str = '', checkboxText: str = '') -> None` *static* | Informational alert with an OK button. A minor alert is less intrusive (no icon emphasis). |
| `Critical(text: str, advice: str = '') -> None` *static* | Error alert with an OK button. |
| `Question(question: str, advice: str = '', defaultButton: AlertButton = AlertButton.Ok, okText: str = '', cancelText: str = '', buttonAText: str = '', buttonBText: str = '', category: str = '', item: str = '', checkboxText: str = '') -> DialogResult` *static* | Question alert. Empty button texts use the default labels; buttons A and B are shown only with a text. Returns Ok, Cancel, ButtonA or ButtonB. |
| `Confirm(question: str, advice: str = '', okText: str = '', cancelText: str = '', isOkDefault: bool = True) -> bool` *static* | Question alert with two buttons (e.g. okText "Yes", cancelText "No"). Returns `True` when the OK button was chosen. |
| `InformWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink: str = '', isMinor: bool = False, category: str = '', item: str = '', checkboxText: str = '') -> None` *static* | Informational alert whose advice contains a hyperlink: adviceBeforeLink, `[linkTitle](linkURL)`, adviceAfterLink. |
| `CriticalWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink: str = '') -> None` *static* | Error alert whose advice contains a hyperlink. |
| `AreAlertsAllowed() -> bool` *static* | `False` when alerts are suppressed (e.g. while running in batch or automated test mode). |

### TextPair

> **Full name:** `api.TextPair` · **Inherits:** `api.Object`

Values entered in the two-text dialog.

**Constructors**

| Constructor | Description |
|---|---|
| `TextPair()` | Default value (fields at their defaults). |
| `TextPair(fFirst, fSecond)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: TextPair) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: TextPair) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fFirst` | `str` | Text of the first field. |
| `fSecond` | `str` | Text of the second field. |

### StandardDialogs

> **Full name:** `api.StandardDialogs` · **Inherits:** `api.Object`

Ready-made dialogs that edit one or two values or choose from a list (static functions only).

**Constructors**

Not instantiable from Python: use the static methods on the class (`api.StandardDialogs.Method(...)`).

**Methods**

| Method | Description |
|---|---|
| `EditText(title: str, label: str, value: str = '', okText: str = '', cancelText: str = '', helpText: str = '', isEmptyAllowed: bool = True) -> str \| None` *static* | One single-line text field. With isEmptyAllowed `False`, OK stays disabled while the field is empty. |
| `EditMultilineText(title: str, label: str, value: str = '', width: int = 40, height: int = 10, okText: str = '', cancelText: str = '', helpText: str = '', isEmptyAllowed: bool = True) -> str \| None` *static* | One multi-line text field; width in standard characters, height in lines. |
| `EditTwoTexts(title: str, label1: str, label2: str, value1: str = '', value2: str = '', helpText1: str = '', helpText2: str = '', okText: str = '', cancelText: str = '') -> TextPair \| None` *static* | Two single-line text fields. |
| `EditInteger(title: str, label: str, value: int = 0, okText: str = '', cancelText: str = '', helpText: str = '') -> int \| None` *static* | Asks for an integer in a dialog with one field; `None` when the user cancels. |
| `EditReal(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *static* | Plain real number. |
| `EditDimension(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *static* | Length in world units, shown and entered in the document units. |
| `EditAngle(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *static* | Angle in degrees. |
| `EditPoint2D(title: str, label: str, value: Point2D = Point2D(), okText: str = '', cancelText: str = '', helpText: str = '') -> Point2D \| None` *static* | X and Y fields. |
| `EditPoint3D(title: str, label: str, value: Point3D = Point3D(), okText: str = '', cancelText: str = '', helpText: str = '') -> Point3D \| None` *static* | X, Y and Z fields. |
| `ChooseFromList(title: str, label: str, choices: list[str], selectedIndex: int = 0, okText: str = '', cancelText: str = '') -> int \| None` *static* | List of choices; returns the 0-based index of the chosen item. selectedIndex -1 selects nothing. |
| `ChooseManyFromList(title: str, label: str, choices: list[str], selectedIndices: list[int] = [], okText: str = '', cancelText: str = '') -> list[int] \| None` *static* | List of choices with multiple selection; returns the 0-based indices of the chosen items. |

### LayoutDialog

> **Full name:** `api.LayoutDialog` · **Inherits:** `api.Object`

Modal layout manager dialog, built control by control in code. Life cycle (one-shot: a dialog runs at most once):

1. **Construct** — the layout is created with its OK and (optional) Cancel button.
2. **Add controls** — `Add<Control>(controlID, ...)` for every control. IDs are chosen by the caller (3 .. 9999).
3. **Position controls** — `SetFirstItem(controlID)` for the top-left control, then `PlaceBelow` / `PlaceRight` relative to another control. Children of a group box, tab pane or swap pane start with `SetFirstGroupItem(groupControlID, controlID)`. `BindEdges` and `Align*` control resizing.
4. **Register handlers** — `OnSetup`, `OnControl(controlID, handler)`, `OnOk`, `OnCancel`, ... (all optional; handlers are Python callables receiving a `DialogEvent`).
5. **Run** — shows the dialog and blocks until it is closed; returns `DialogResult.Ok` or `DialogResult.Cancel`.
6. **Read values** — the `Get...` functions keep working after `Run`: the values of all controls are captured when the dialog closes.

Value functions (`Set...`, `Select...`, `Add...Item`, ...) may be called at any time after the control was added; calls made before the dialog is shown are queued and applied, in order, right before the Setup handler runs. `Get...` functions return `None` before the dialog is shown.

Indices of choices, list browser rows/columns and tab panes are 0-based. Tree items are identified by the ID returned from `AddTreeItem`; the root parent is -1. `controlID`, `referenceControlID`, `groupControlID`, `paneControlID`, `tabControlID` and `swapControlID` identify controls; `alignmentGroupID` is a shared edge-alignment identifier, not a control; `itemID` and `parentID` identify items within a tree control.

**Constructors**

| Constructor | Description |
|---|---|
| `LayoutDialog(title: str, okText: str = '', cancelText: str = '', hasCancel: bool = True, isWidthResizable: bool = False, isHeightResizable: bool = False)` | Empty okText/cancelText use the default "OK"/"Cancel" labels; hasCancel `False` shows only the OK button. |

**Methods**

*Life cycle*

| Method | Description |
|---|---|
| `IsValid() -> bool` | True when this object refers to an existing layout dialog (the layout was created and has not run yet, or is running). |
| `GetDialogID() -> int` | Returns the dialog ID (layout manager ID (0 when the layout could not be created)). |
| `IsRunning() -> bool` | True between the Setup event and the return of `Run`. |
| `WasRun() -> bool` | True when `Run` has returned. |
| `Run(helpID: str = '') -> DialogResult` | Shows the dialog and blocks until it is closed; returns `DialogResult.Ok` or `DialogResult.Cancel`, or `DialogResult.None_` when the dialog was already run or its layout is not valid. `helpID` is the contextual help identifier. |
| `Close(isOk: bool = True) -> bool` | Closes the running dialog from an event handler as if OK (isOk) or Cancel was pressed. The OnOk / OnCancel handlers are not called. Returns `False` outside of an event handler. |
| `CancelClose() -> None` | From an OnOk or OnCancel handler: keep the dialog open (e.g. after a validation error). |

*Event handlers*

| Method | Description |
|---|---|
| `OnSetup(handler: callable(DialogEvent)) -> None` | Registers `handler`, called when the dialog is set up, right before it is shown. |
| `OnSetdown(handler: callable(DialogEvent)) -> None` | Registers `handler`, called when the dialog is closing. |
| `OnOk(handler: callable(DialogEvent)) -> None` | Registers `handler`, called when OK is pressed (call `CancelClose()` in it to keep the dialog open). |
| `OnCancel(handler: callable(DialogEvent)) -> None` | Registers `handler`, called when Cancel is pressed (call `CancelClose()` in it to keep the dialog open). |
| `OnResize(handler: callable(DialogEvent)) -> None` | Registers `handler`, called when the dialog is resized. |
| `OnEditLostFocus(handler: callable(DialogEvent)) -> None` | Registers `handler`, called when an edit field loses the focus. |
| `OnControl(controlID: int, handler: callable(DialogEvent)) -> None` | Registers `handler`, called when the control `controlID` changes or is clicked. |
| `OnAnyEvent(handler: callable(DialogEvent)) -> None` | Called before the specific handler for every event, including Timer and Other. |
| `GetListBrowserEvent(controlID: int) -> ListBrowserEvent` | Detail of the last event of a list browser (valid inside its OnControl handler). |

*Positioning (before Run)*

| Method | Description |
|---|---|
| `SetFirstItem(controlID: int) -> bool` | Sets the first item of control `controlID`. |
| `SetFirstGroupItem(groupControlID: int, controlID: int) -> bool` | Sets the first group item of control `controlID`. |
| `PlaceBelow(referenceControlID: int, controlID: int, indent: int = 0, spacing: int = 0) -> bool` | Indent in standard characters, spacing in lines (below) or characters (right). |
| `PlaceRight(referenceControlID: int, controlID: int, indent: int = 0, spacing: int = 0) -> bool` | Places `controlID` to the right of `referenceControlID`. Indent in standard characters, spacing in lines (below) or characters (right). |
| `BindEdges(controlID: int, isLeft: bool, isRight: bool, isTop: bool, isBottom: bool) -> bool` | Which edges follow the dialog edges when a resizable dialog is resized. |
| `BindProportional(controlID: int, isLeft: bool, isRight: bool, isTop: bool, isBottom: bool) -> bool` | Like `BindEdges`, but the chosen edges of `controlID` move proportionally when a resizable dialog is resized. |
| `AlignLeft(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | Assigns controlID to an alignment group for the specified edge, not to another control. Controls with the same alignmentGroupID align their corresponding edges together. No control or group box with alignmentGroupID needs to exist; choose a positive signed-16-bit ID. isResizing `False` shifts the control; `True` resizes it to satisfy the alignment. |
| `AlignRight(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | Aligns the right edge of `controlID` with the other members of the alignment group `alignmentGroupID` (an alignment identifier, not a control). |
| `AlignBottom(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | Aligns the bottom edge of `controlID` with the other members of the alignment group `alignmentGroupID` (an alignment identifier, not a control). |
| `SetControlSize(controlID: int, widthInPixels: int, heightInPixels: int) -> bool` | Sets the control size of control `controlID`. |

*Dialog*

| Method | Description |
|---|---|
| `SetDialogSize(size: DialogSize) -> bool` | Sets the dialog size. |
| `GetDialogSize() -> DialogSize \| None` | Returns the dialog size. |
| `SetDialogPosition(left: int, top: int) -> bool` | Sets the dialog position. |

*Control creation (before Run)*

| Method | Description |
|---|---|
| `AddStaticText(controlID: int, text: str, width: int = -1, style: StaticTextStyle = StaticTextStyle.Regular) -> bool` | Adds a static text (`width` in characters, -1 = fit the text) in the style `style`. |
| `AddCenteredStaticText(controlID: int, text: str, width: int = -1) -> bool` | Adds a centered static text (`width` in characters, -1 = fit the text). |
| `AddRightStaticText(controlID: int, text: str, width: int = -1) -> bool` | Adds a right-aligned static text (`width` in characters, -1 = fit the text). |
| `AddEditText(controlID: int, text: str = '', width: int = 20, heightInLines: int = 1) -> bool` | Adds a text field with the initial `text` (`width` in characters, `heightInLines` > 1 for a multi-line field). |
| `AddEditInteger(controlID: int, value: int = 0, width: int = 10) -> bool` | Adds an integer field with the initial `value`. |
| `AddEditReal(controlID: int, value: float = 0.0, type: EditRealType = EditRealType.Real, width: int = 10) -> bool` | Adds a real number field with the initial `value`; `type` selects plain numbers, dimensions, angles, ... |
| `AddEditPassword(controlID: int, width: int = 20) -> bool` | Adds a password field (the text is hidden). |
| `AddSearchBox(controlID: int, prompt: str = '', width: int = 20) -> bool` | Adds a search box showing `prompt` while empty. |
| `AddPushButton(controlID: int, text: str) -> bool` | Adds a push button labeled `text`. |
| `AddCheckBox(controlID: int, text: str) -> bool` | Adds a check box labeled `text`. |
| `AddThreeStateCheckBox(controlID: int, text: str) -> bool` | Adds a check box with an additional indeterminate state. |
| `AddRadioButton(controlID: int, text: str) -> bool` | Adds a radio button labeled `text`. |
| `AddGroupBox(controlID: int, text: str = '', hasFrame: bool = True) -> bool` | Adds a group box (a container for other controls) titled `text`, with or without a frame. |
| `AddCheckBoxGroupBox(controlID: int, text: str, hasFrame: bool = True) -> bool` | Adds a group box with a check box in its title; the check box enables the contents. |
| `AddRadioButtonGroupBox(controlID: int, text: str, hasFrame: bool = True) -> bool` | Adds a group box with a radio button in its title. |
| `AddPullDownMenu(controlID: int, width: int = 20) -> bool` | Adds a pull-down menu (fill it with `AddChoice` / `SetChoices`). |
| `AddListBox(controlID: int, width: int = 20, heightInLines: int = 8, isMultiSelect: bool = False) -> bool` | Adds a list box (`isMultiSelect` for multiple selection). |
| `AddListBrowser(controlID: int, width: int = 40, heightInLines: int = 10) -> bool` | Adds a list browser (a table with columns; see the list browser functions). |
| `AddTreeControl(controlID: int, width: int = 40, heightInLines: int = 10) -> bool` | Adds a tree control (see the tree functions). |
| `AddTabControl(controlID: int) -> bool` | Adds a tab control; add its panes with `AddTabPane`. |
| `AddTabPane(tabControlID: int, paneControlID: int) -> bool` | Adds the group box paneControlID (its text is the tab label) as a pane of the tab control. |
| `AddSwapControl(controlID: int) -> bool` | Adds a swap control (panes shown one at a time); add its panes with `AddSwapPane`. |
| `AddSwapPane(swapControlID: int, paneControlID: int) -> bool` | Adds the group box paneControlID as a pane of the swap control. |
| `AddSeparator(controlID: int, widthInPixels: int = 0) -> bool` | Adds a horizontal separator line (`widthInPixels` 0 = default width). |
| `AddColorPopup(controlID: int, width: int = -1) -> bool` | Adds a color pop-up (document color palette). |
| `AddPatternPopup(controlID: int) -> bool` | Adds a pattern pop-up. |
| `AddLineWeightPopup(controlID: int) -> bool` | Adds a line weight pop-up. |
| `AddClassPullDown(controlID: int, width: int = 30, isShowingDefaultItems: bool = True) -> bool` | Adds a pull-down listing the classes of the document (with the default items when `isShowingDefaultItems`). |
| `AddLayerPullDown(controlID: int, width: int = 30, isShowingDefaultItems: bool = True) -> bool` | Adds a pull-down listing the layers of the document (with the default items when `isShowingDefaultItems`). |
| `AddColorButton(controlID: int, color: ColorRGB = ColorRGB()) -> bool` | Push button that opens the system color picker; the chosen color is reported in `DialogEvent.fData`. |
| `AddSlider(controlID: int, maximum: int = 100) -> bool` | Adds a slider ranging from 0 to `maximum`. |
| `AddImage(controlID: int, widthInPixels: int, heightInPixels: int, imageSpecifier: str) -> bool` | ImageSpecifier: resource image path such as "Vectorworks/Images/Name.png". |
| `HasControl(controlID: int) -> bool` | True when a control with the ID `controlID` was added. |

*Any control*

| Method | Description |
|---|---|
| `Enable(controlID: int, isEnabled: bool = True) -> bool` | Enables or disables the control `controlID`. |
| `Show(controlID: int, isVisible: bool = True) -> bool` | Shows or hides the control `controlID`. |
| `IsEnabled(controlID: int) -> bool \| None` | True when the control `controlID` is enabled. |
| `IsVisible(controlID: int) -> bool \| None` | True when the control `controlID` is visible. |
| `SetFocus(controlID: int) -> bool` | Sets the focus of control `controlID`. |
| `SetHelpText(controlID: int, helpText: str) -> bool` | Sets the help text of control `controlID`. |
| `SetToolTip(controlID: int, toolTip: str, subToolTip: str = '') -> bool` | Sets the tool tip of control `controlID`. |
| `SetIndeterminate(controlID: int, isIndeterminate: bool = True) -> bool` | Sets the indeterminate of control `controlID`. |

*Text: static texts, edit fields, buttons, check boxes, group boxes*

| Method | Description |
|---|---|
| `SetText(controlID: int, text: str) -> bool` | Sets the text of control `controlID`. |
| `GetText(controlID: int) -> str \| None` | Returns the text of control `controlID`. |
| `SetTextEditable(controlID: int, isEditable: bool) -> bool` | Sets the text editable of control `controlID`. |
| `SelectAllText(controlID: int) -> bool` | Selects the whole text of the edit field `controlID`. |
| `SetTextSelection(controlID: int, start: int, end: int) -> bool` | Sets the text selection of control `controlID`. |
| `SetStaticTextStyle(controlID: int, style: StaticTextStyle) -> bool` | Sets the static text style of control `controlID`. |
| `SetStaticTextColor(controlID: int, color: ColorRGB) -> bool` | Sets the static text color of control `controlID`. |

*Check boxes, radio buttons, check box / radio group boxes*

| Method | Description |
|---|---|
| `SetBool(controlID: int, value: bool) -> bool` | Sets the bool of control `controlID`. |
| `GetBool(controlID: int) -> bool \| None` | Whether *Bool* is on of control `controlID`. |
| `SetCheckState(controlID: int, state: CheckState) -> bool` | Sets the check state of control `controlID`. |
| `GetCheckState(controlID: int) -> CheckState \| None` | Returns the check state of control `controlID`. |

*Numbers*

| Method | Description |
|---|---|
| `SetInteger(controlID: int, value: int) -> bool` | Sets the integer of control `controlID`. |
| `GetInteger(controlID: int) -> int \| None` | Returns the integer of control `controlID`. |
| `SetReal(controlID: int, value: float) -> bool` | Lengths and coordinates in world units, angles in degrees (the type is the one given to AddEditReal). |
| `GetReal(controlID: int) -> float \| None` | Returns the real of control `controlID`. Lengths and coordinates in world units, angles in degrees (the type is the one given to AddEditReal). |

*Choices: pull-down menus, list boxes, class/layer pull-downs*

| Method | Description |
|---|---|
| `AddChoice(controlID: int, text: str, index: int = -1) -> bool` | Index -1 appends. |
| `SetChoices(controlID: int, choices: list[str]) -> bool` | Sets the choices of control `controlID`. |
| `RemoveChoice(controlID: int, index: int) -> bool` | Removes the choice at `index` of a pull-down menu or list box. |
| `RemoveAllChoices(controlID: int) -> bool` | Removes every choice of a pull-down menu or list box. |
| `GetChoiceCount(controlID: int) -> int \| None` | Number of choice items of control `controlID`. |
| `GetChoiceText(controlID: int, index: int) -> str \| None` | Returns the choice text for `controlID`, `index`. |
| `FindChoice(controlID: int, text: str) -> int \| None` | Index of the choice with the text `text`; `None` when there is none. |
| `SelectChoice(controlID: int, index: int, isSelected: bool = True) -> bool` | Selects (or, with `isSelected=False`, deselects) the choice at `index`. |
| `SelectChoiceByText(controlID: int, text: str) -> bool` | Selects the choice with the text `text`. |
| `GetSelectedChoice(controlID: int) -> int \| None` | First selected index, -1 when nothing is selected. |
| `GetSelectedChoiceText(controlID: int) -> str \| None` | Returns the selected choice text of control `controlID`. |
| `GetSelectedChoices(controlID: int) -> list[int] \| None` | All selected indices of a multi-selection list box. |

*Attribute controls*

| Method | Description |
|---|---|
| `SetColorButton(controlID: int, color: ColorRGB) -> bool` | Sets the color button of control `controlID`. |
| `GetColorButton(controlID: int) -> ColorRGB \| None` | Returns the color button of control `controlID`. |
| `SetColorIndex(controlID: int, colorIndex: int) -> bool` | Index into the document color table (color popup). |
| `GetColorIndex(controlID: int) -> int \| None` | Returns the color index of control `controlID`. Index into the document color table (color popup). |

*Pattern popup*

| Method | Description |
|---|---|
| `SetPatternIndex(controlID: int, patternIndex: int) -> bool` | Pattern index (0 none, 1 background, 2 foreground, ...). |
| `GetPatternIndex(controlID: int) -> int \| None` | Returns the pattern index of control `controlID`. Pattern index (0 none, 1 background, 2 foreground, ...). |
| `SetLineWeight(controlID: int, lineWeight: int) -> bool` | Line weight popup, in mils. |
| `GetLineWeight(controlID: int) -> int \| None` | Returns the line weight of control `controlID`. Line weight popup, in mils. |

*Slider and image*

| Method | Description |
|---|---|
| `SetSliderValue(controlID: int, value: int) -> bool` | Sets the slider value of control `controlID`. |
| `GetSliderValue(controlID: int) -> int \| None` | Returns the slider value of control `controlID`. |
| `SetSliderLiveUpdate(controlID: int, isLive: bool) -> bool` | Sets the slider live update of control `controlID`. |
| `SetSliderTickMarks(controlID: int, count: int) -> bool` | Sets the slider tick marks of control `controlID`. |
| `SetImage(controlID: int, imageSpecifier: str) -> bool` | Sets the image of control `controlID`. |

*Tab and swap controls*

| Method | Description |
|---|---|
| `ShowTabPane(tabControlID: int, paneControlID: int) -> bool` | Brings the pane `paneControlID` of the tab control `tabControlID` to the front. |
| `ShowSwapPane(swapControlID: int, paneControlID: int) -> bool` | Shows the pane `paneControlID` of the swap control `swapControlID`. |
| `GetActivePane(controlID: int) -> int \| None` | Control ID of the group box for the visible pane. |

*List browser*

| Method | Description |
|---|---|
| `AddListBrowserColumn(controlID: int, header: str, widthInPixels: int = 100, column: int = -1) -> bool` | Column -1 appends; width in pixels. Returns `False` when the control is not a list browser. |
| `RemoveListBrowserColumn(controlID: int, column: int) -> bool` | Removes the column `column` of the list browser. |
| `GetListBrowserColumnCount(controlID: int) -> int \| None` | Number of list browser column items of control `controlID`. |
| `SetListBrowserColumnWidth(controlID: int, column: int, widthInPixels: int) -> bool` | Sets the list browser column width of control `controlID`. |
| `SetListBrowserColumnControl(controlID: int, column: int, controlType: ListBrowserControlType) -> bool` | Sets the list browser column control of control `controlID`. |
| `SetListBrowserColumnDisplay(controlID: int, column: int, itemDisplay: ListBrowserDisplayType, editDisplay: ListBrowserDisplayType = ListBrowserDisplayType.TextOnly) -> bool` | Sets the list browser column display of control `controlID`. |
| `AddListBrowserColumnChoice(controlID: int, column: int, text: str, imageOn: int = -1, imageOff: int = -1, data: int = 0) -> bool` | Value a MultiState / SingleInstance / Radio cell may take; returns `False` on failure. |
| `SetListBrowserCellChoice(controlID: int, row: int, column: int, choiceIndex: int) -> bool` | Sets the cell to one of the values added with AddListBrowserColumnChoice. |
| `AddListBrowserRow(controlID: int, text: str, row: int = -1) -> bool` | Row -1 appends. text is the first column text. |
| `AddListBrowserRowCells(controlID: int, cells: list[str]) -> bool` | Appends a row with one text per column. |
| `RemoveListBrowserRow(controlID: int, row: int) -> bool` | Removes the row `row` of the list browser. |
| `RemoveAllListBrowserRows(controlID: int) -> bool` | Removes every row of the list browser. |
| `GetListBrowserRowCount(controlID: int) -> int \| None` | Number of list browser row items of control `controlID`. |
| `SetListBrowserCell(controlID: int, row: int, column: int, text: str, imageIndex: int = -1) -> bool` | Sets the list browser cell of control `controlID`. |
| `GetListBrowserCell(controlID: int, row: int, column: int) -> str \| None` | Returns the list browser cell for `controlID`, `row`, `column`. |
| `SetListBrowserCellData(controlID: int, row: int, column: int, data: int) -> bool` | Sets the list browser cell data of control `controlID`. |
| `GetListBrowserCellData(controlID: int, row: int, column: int) -> int \| None` | Returns the list browser cell data for `controlID`, `row`, `column`. |
| `SetListBrowserCellCheckState(controlID: int, row: int, column: int, state: CheckState) -> bool` | Sets the list browser cell check state of control `controlID`. |
| `GetListBrowserCellCheckState(controlID: int, row: int, column: int) -> CheckState \| None` | Returns the list browser cell check state for `controlID`, `row`, `column`. |
| `SetListBrowserCellTextColor(controlID: int, row: int, column: int, color: ColorRGB) -> bool` | Sets the list browser cell text color of control `controlID`. |
| `SetListBrowserCellReadOnly(controlID: int, row: int, column: int, isReadOnly: bool = True) -> bool` | Sets the list browser cell read only of control `controlID`. |
| `SetListBrowserReadOnly(controlID: int, isReadOnly: bool = True) -> bool` | Sets the list browser read only of control `controlID`. |
| `SelectListBrowserRows(controlID: int, firstRow: int, lastRow: int, isSelected: bool = True) -> bool` | Selects (or deselects) the rows `firstRow` .. `lastRow`. |
| `IsListBrowserRowSelected(controlID: int, row: int) -> bool \| None` | True when the row `row` of the list browser is selected. |
| `GetListBrowserSelectedRows(controlID: int) -> list[int] \| None` | Returns the list browser selected rows of control `controlID`. |
| `EnableListBrowserSorting(controlID: int, isEnabled: bool = True) -> bool` | Lets the user sort the rows by clicking a column header. |
| `SetListBrowserSortColumn(controlID: int, column: int, isAscending: bool = True) -> bool` | Sets the list browser sort column of control `controlID`. |
| `EnableListBrowserSingleSelection(controlID: int, isEnabled: bool = True) -> bool` | Restricts the list browser to the selection of one row. |
| `EnableListBrowserDragAndDrop(controlID: int, isEnabled: bool = True) -> bool` | Lets the user reorder the rows by drag and drop. |
| `ShowListBrowserHeader(controlID: int, isVisible: bool = True) -> bool` | Shows or hides the column header row. |
| `EnsureListBrowserRowVisible(controlID: int, row: int) -> bool` | Scrolls the list browser so that the row `row` is visible. |
| `EnableListBrowserUpdates(controlID: int, isEnabled: bool) -> bool` | Suspends redrawing while many rows are changed; call again with `True` and RefreshListBrowser. |
| `RefreshListBrowser(controlID: int) -> bool` | Redraws the list browser (after updates were suspended with `EnableListBrowserUpdates`). |

*Tree control*

| Method | Description |
|---|---|
| `AddTreeItem(controlID: int, text: str, parentID: int = -1) -> int \| None` | Appends an item under parentID (-1 = root). Returns the new item ID, or `None` when the dialog is not running (tree items can only be added from the Setup handler or later). |
| `RemoveTreeItem(controlID: int, itemID: int) -> bool` | Removes the tree item `itemID` and its children. |
| `RemoveAllTreeItems(controlID: int) -> bool` | Removes every tree item. |
| `GetTreeItemText(controlID: int, itemID: int) -> str \| None` | Returns the tree item text for `controlID`, `itemID`. |
| `GetTreeItemParent(controlID: int, itemID: int) -> int \| None` | Returns the tree item parent for `controlID`, `itemID`. |
| `GetTreeItemChildren(controlID: int, itemID: int) -> list[int] \| None` | Returns the tree item children for `controlID`, `itemID`. |
| `SetTreeItemData(controlID: int, itemID: int, data: int) -> bool` | Sets the tree item data of control `controlID`. |
| `GetTreeItemData(controlID: int, itemID: int) -> int \| None` | Returns the tree item data for `controlID`, `itemID`. |
| `SetTreeItemCheckState(controlID: int, itemID: int, state: CheckState, isClickable: bool = True) -> bool` | Sets the tree item check state of control `controlID`. |
| `GetTreeItemCheckState(controlID: int, itemID: int) -> CheckState \| None` | Returns the tree item check state for `controlID`, `itemID`. |
| `ExpandTreeItem(controlID: int, itemID: int, isExpanded: bool = True) -> bool` | Expands (or, with `isExpanded=False`, collapses) the tree item `itemID`. |
| `IsTreeItemExpanded(controlID: int, itemID: int) -> bool \| None` | True when the tree item `itemID` is expanded. |
| `SelectTreeItem(controlID: int, itemID: int) -> bool` | Selects the tree item `itemID`. |
| `GetSelectedTreeItem(controlID: int) -> int \| None` | -1 when nothing is selected. |
| `GetSelectedTreeItems(controlID: int) -> list[int] \| None` | Returns the selected tree items of control `controlID`. |
| `EnableTreeMultiSelection(controlID: int, isEnabled: bool = True) -> bool` | Allows the selection of several tree items. |

## Enumerations

### DialogResult

> **Full name:** `api.DialogResult` · **Kind:** `IntEnum`

How a dialog or an alert was closed.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` | The dialog could not be shown. |
| `Ok` | `1` | The default (OK) button. |
| `Cancel` | `2` | The Cancel button, Escape or the close box. |
| `ButtonA` | `3` | Custom button A of a question alert. |
| `ButtonB` | `4` | Custom button B of a question alert. |

### AlertButton

> **Full name:** `api.AlertButton` · **Kind:** `IntEnum`

Default button of a question alert.

| Member | Value | Description |
|---|---|---|
| `Cancel` | `0` |  |
| `Ok` | `1` |  |
| `ButtonA` | `2` |  |
| `ButtonB` | `3` |  |

### EditRealType

> **Full name:** `api.EditRealType` · **Kind:** `IntEnum`

Kind of value shown by a real number edit field. Lengths and coordinates are passed in world units (mm); the field displays and parses them in the document units.

| Member | Value | Description |
|---|---|---|
| `Real` | `1` | Plain number. |
| `Angle` | `2` | Angle in degrees. |
| `Dimension` | `3` | Length in world units. |
| `CoordinateX` | `4` | X coordinate (respects the user origin). |
| `CoordinateY` | `5` | Y coordinate (respects the user origin). |

### StaticTextStyle

> **Full name:** `api.StaticTextStyle` · **Kind:** `IntEnum`

Font style of a static text.

| Member | Value | Description |
|---|---|---|
| `Regular` | `0` |  |
| `Caption` | `1` |  |
| `Bold` | `2` |  |
| `Reduced` | `3` | Small system font (macOS), regular size on Windows. |

### CheckState

> **Full name:** `api.CheckState` · **Kind:** `IntEnum`

State of a three-state check box, a list browser cell or a tree item check box.

| Member | Value | Description |
|---|---|---|
| `Off` | `0` |  |
| `On` | `1` |  |
| `Mixed` | `2` |  |

### DialogEventType

> **Full name:** `api.DialogEventType` · **Kind:** `IntEnum`

Kind of a dialog event (see DialogEvent).

| Member | Value | Description |
|---|---|---|
| `Setup` | `0` | The dialog is about to be shown; initialize controls here. |
| `Setdown` | `1` | The dialog is about to be destroyed. |
| `Ok` | `2` | The OK (default) button was pressed; call `LayoutDialog.CancelClose` to keep it open. |
| `Cancel` | `3` | The Cancel button was pressed; call `LayoutDialog.CancelClose` to keep it open. |
| `Control` | `4` | A control changed or was clicked (fControlID, fData). |
| `Resize` | `5` | The user resized the dialog. |
| `Timer` | `6` | Timer tick. |
| `EditLostFocus` | `7` | An edit field lost the keyboard focus. |
| `Other` | `8` | Any other layout manager message (fData holds the raw message code). |

### ListBrowserControlType

> **Full name:** `api.ListBrowserControlType` · **Kind:** `IntEnum`

Behavior of a list browser column.

| Member | Value | Description |
|---|---|---|
| `None_` | `1` | Plain text or image cells. |
| `Radio` | `2` | One checked cell per column. |
| `MultiState` | `3` | Clicking cycles through the column data items. |
| `SingleInstance` | `4` | Clicking toggles the cell between the column data items 0 and 1. |
| `NoClick` | `5` | Cells do not react to clicks. |
| `Number` | `6` | Editable number cells. |
| `MultipleImages` | `7` | Several images per cell. |
| `DiscTriangle` | `8` | Expand/collapse triangle (hierarchical rows). |

### ListBrowserDisplayType

> **Full name:** `api.ListBrowserDisplayType` · **Kind:** `IntEnum`

What a list browser column shows.

| Member | Value | Description |
|---|---|---|
| `ImageOnly` | `1` |  |
| `TextOnly` | `2` |  |
| `ImageAndText` | `3` |  |

### ListBrowserEventType

> **Full name:** `api.ListBrowserEventType` · **Kind:** `IntEnum`

What happened in a list browser (see `LayoutDialog.GetListBrowserEvent`).

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `DataChangeClick` | `1` |  |
| `DataChangeAllClick` | `2` |  |
| `SelectionChangeClick` | `3` |  |
| `DoubleClick` | `4` |  |
| `DeleteKeyPressed` | `5` |  |
| `UpKey` | `6` |  |
| `DownKey` | `7` |  |
| `AlphaNumericKey` | `8` |  |
| `SortOccurred` | `9` |  |
| `SelectionMultChangeClick` | `10` |  |
| `EnterKey` | `11` |  |
| `DataChangeRecursiveClick` | `12` |  |
| `DoubleAllClick` | `13` |  |
| `DoubleRecursiveClick` | `14` |  |
| `ReceivingDragAndDrop` | `15` |  |
| `DragAndDrop` | `16` |  |

---

[Back to the index](README.md) · [Back to top](#uilayoutcreate--alerts-standard-dialogs-and-layout-dialogs)

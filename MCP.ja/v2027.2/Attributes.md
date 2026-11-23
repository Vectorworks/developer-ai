[English](../../MCP/v2027.2/Attributes.md) • [Deutsch](../../MCP.de/v2027.2/Attributes.md) • **日本語**

# Attributes — マーカーとドロップシャドウ

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

マーカーとドロップシャドウの値の形式です。クラスとオブジェクトのグラフィック属性、およびファイルのデフォルト属性を読み書きするツールで共通して使用します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [マーカー](#line-end-markers)
- [ドロップシャドウ](#drop-shadow)

<a id="overview"></a>

## 概要

| 形式 | 使用するツール | 概要 |
|---|---|---|
| [マーカー](#line-end-markers) | [`editClass`](DocumentAccess.md#editclass), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes), [`setPreferences`](DocumentAccess.md#setpreferences) | 直線、円弧、曲線、多角形、およびマーカーを使用できるプラグインオブジェクトの始点と終点に付ける、矢印、斜線などのマーカーです。 |
| [ドロップシャドウ](#drop-shadow) | [`editClass`](DocumentAccess.md#editclass), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | オブジェクトの背後に描画するドロップシャドウです。 |

どちらの形式も**部分指定**です。指定したメンバーだけを変更し、その他のメンバーは値を維持します。元になる保存済みのマーカーやドロップシャドウがない場合、省略したメンバーは各形式の説明に記載したデフォルト値から始まります。オブジェクトではない値はどのメンバーも変更しませんが、書き込みは行われます（`setObjectAttributes`の`dropShadow`に、真偽値でもオブジェクトでもない値を指定した場合を除きます）。`applied`はその書き込みを報告し、`setObjectAttributes`と`setPreferences`では、オブジェクトではないマーカーは現在のマーカーを書き戻すため、他のマーカーの書き込みと同様に`byClass`／`markersByClass`をオフにします。変更しない場合は、そのメンバーを省略してください。

読み取ったマーカーやドロップシャドウは、メンバーを1つだけ編集してそのまま送り返すことができます。読み取ったときの値のままのメンバーは、再度適用されないためです。

- 現在の太さと等しい`thickness`は、`thicknessBasis`を`custom`にしません。
- 現在の値と等しい`thicknessBasis`は無視されるため、`thickness`の変更を打ち消すことはできません。
- `color`と`colorIndex`のうち、現在の色と等しい形式は無視されます。両方が変更される場合は、`colorIndex`が優先されます。

誤った値はエラーになりません。JSONの型が誤っている数値は無視され、そのメンバーは値を維持します。型が誤っている真偽値（`tail`、`visible`、`enabled`）は`false`になります。不明な名前や文字列ではない名前は、各メンバーの説明に従って処理されます。

<a id="line-end-markers"></a>

## マーカー

マーカーは次のメンバーを持つオブジェクトです。すべて省略可能です。

| メンバー | 型 | 説明 |
|---|---|---|
| `shape` | string | マーカーの形状。次のいずれか: `arrow`, `concaveCurvedArrow`, `circle`, `dimSlash`, `dimCross`, `lasso`, `hexagon`, `vShaped`, `cone`, `taperedVShaped`, `sShaped`, `rectangle`, `doubleLine`。不明な名前の場合は現在の形状を維持します。 |
| `fill` | string | `lineColor`はマーカーの面を線の色で、`white`は白で塗りつぶし、`none`は面を塗りつぶしません。次のいずれか: `lineColor`, `white`, `none`。その他の文字列は`lineColor`になります。 |
| `base` | string | マーカーの底辺の形状。次のいずれか: `flat`, `open`, `angle`, `arc`。その他の文字列は`flat`になります。 |
| `halfTick` | string | マーカー全体、または左半分か右半分だけ（半欠け）を描画します。次のいずれか: `full`, `left`, `right`。不明な名前の場合は現在の値を維持します。 |
| `tail` | boolean | マーカーに尾部を追加します（マーカー編集ダイアログの「反転」）。 |
| `angle` | integer | 開き角度。整数の度単位です。符号付き8ビットの数値として保存されるため、200は-56になります。 |
| `length` | number | 長さ。用紙上のインチ単位です。 |
| `width` | number | 幅。用紙上のインチ単位です。 |
| `thickness` | number | マーカーの線の太さ。単位は`thicknessUnits`で指定します。太さを変更すると`thicknessBasis`が`custom`になります。0～255の整数ミル（約6.5 mmまたは18.4ポイント）として保存されます。値は整数ミルに丸められ、それより大きい値は循環します（300ミルは44ミルになります）。 |
| `thicknessBasis` | string | 太さの基準。オブジェクトの線の太さ、寸法線の太さ、またはカスタムの`thickness`です。次のいずれか: `lineThickness`, `dimThickness`, `custom`。不明な名前の場合は現在の値を維持します。 |
| `thicknessUnits` | string | `thickness`の単位。次のいずれか: `mils`, `points`, `millimeters`。不明な名前の場合は現在の値を維持します。 |
| `visible` | boolean | マーカーを表示します。クラスには保存されません。`editClass`はこの値を無視し、`getClasses`はクラスのマーカーについて常に`true`を返します。オブジェクトではマーカーとともに保存されるため、`beginning`と`end`でも設定されます。`markers.beginningVisible`と`markers.endVisible`では個別に設定できます。 |

元になる保存済みのマーカーがない場合、省略したメンバーは次の値から始まります: `shape` `arrow`、`fill` `lineColor`、`base` `flat`、`halfTick` `full`、`tail` `false`、`angle` 15、`length` 0.125、`width` 0.125、`thickness` 0、`thicknessBasis` `lineThickness`、`thicknessUnits` `mils`、`visible` `false`。

Vectorworksは書き込み時にマーカーを補正します。`arrow`、`concaveCurvedArrow`、`cone`の`width`は常に0になり、一部の形状では`base`、`tail`、`fill`、`angle`がリセットされます。`fill`が`lineColor`（デフォルト）の`cone`は、`fill`が`none`の`arrow`として保存されるため、`cone`は`fill`を`white`または`none`にして指定してください。保存された値は、マーカーを読み取り直して確認してください。

**例**: 直線の終点にある塗りつぶしなしの矢印を、少し長くします。

```json
{
  "uuid": "<uuid>",
  "markers": {
    "end": {"shape": "arrow", "fill": "none", "length": 0.2, "angle": 20},
    "endVisible": true
  }
}
```

**この形式を使用する場所**

| ツール | 引数 |
|---|---|
| [`editClass`](DocumentAccess.md#editclass) | `beginningMarker` |
| [`editClass`](DocumentAccess.md#editclass) | `endMarker` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `markers.beginning` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `markers.end` |
| [`setPreferences`](DocumentAccess.md#setpreferences) | `values.beginningMarker`（`category`が`defaultAttributes`の場合） |
| [`setPreferences`](DocumentAccess.md#setpreferences) | `values.endMarker`（`category`が`defaultAttributes`の場合） |

**マーカーの読み取りと書き込み**

[`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes)の`markers`では、`beginningVisible`と`endVisible`（他のメンバーを変更せずにマーカーを表示／非表示にします）、および`byClass`（クラスのマーカーを使用します）も指定できます。メンバーは`beginning`、`end`、`beginningVisible`、`endVisible`、`byClass`の順に適用されます。

- マーカーを付けられるのは、直線、円弧、曲線、多角形、およびマーカーを使用できるプラグインオブジェクトだけです。円やその他のオブジェクトはマーカーを受け付けず、`applied`は`false`を返します。
- 書き込むマーカーは、オブジェクトの現在のマーカーから始まります。読み取れるマーカーがない場合は上記のデフォルト値から始まるため、`visible`が`true`であるか、同じ呼び出しで対応する`beginningVisible`または`endVisible`が`true`でない限り、非表示のままになります。
- `beginning`または`end`を書き込むと、そのオブジェクトの`byClass`はオフになります。`byClass`は`true`の場合にのみ有効で、最後に適用されるため、両方を指定した場合は`byClass`が優先されます。`byClass: false`は何もしません。
- `beginningVisible`と`endVisible`には、読み取れるマーカーが必要です。同じ呼び出しで先に書き込んだマーカーも含まれます。マーカーがない場合、`applied`は`false`を返します。
- `applied`には、指定したメンバーに応じてキー`beginningMarker`、`endMarker`、`beginningMarkerVisible`、`endMarkerVisible`、`markersByClass`が含まれます。`markersByClass`は`byClass`が`true`の場合にのみ含まれます。

[`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes)は、`beginning`、`end`、`beginningVisible`、`endVisible`（それぞれ、オブジェクトに読み取れるマーカーがある場合のみ）と、常に`byClass`を含む`markers`を返します。[`getClasses`](DocumentAccess.md#getclasses)（`detailed`）は、クラスのマーカーを同じ形式で返します。[`getPreferences`](DocumentAccess.md#getpreferences)（`defaultAttributes`）は、`beginningMarker`、`endMarker`（実際の`visible`フラグ付き）と`markersByClass`を返します。[`setPreferences`](DocumentAccess.md#setpreferences)は、`beginningMarker`と`endMarker`を現在のデフォルトのマーカーから始まる部分指定のマーカーとして書き込み、`markersByClass`（`true`の場合にのみ有効）を書き込みます。`beginningMarker`または`endMarker`を書き込むと`markersByClass`はオフになります。`markersByClass`はそれらの後に適用されるため、両方を指定した場合は`markersByClass`が優先されます。

<a id="drop-shadow"></a>

## ドロップシャドウ

ドロップシャドウは次のメンバーを持つオブジェクトです。すべて省略可能です。

| メンバー | 型 | 説明 |
|---|---|---|
| `enabled` | boolean | ドロップシャドウを描画します。 |
| `units` | string | `offset`と`blurRadius`の単位。用紙上のインチ（`page`、UIの縮尺無視）またはワールド単位（`world`、UIの縮尺追従）です。次のいずれか: `page`, `world`。その他の文字列は`page`になります。 |
| `offset` | number | オブジェクトから影までの距離。単位は`units`で指定します。 |
| `blurRadius` | number | ぼかしの半径。単位は`units`で指定します。 |
| `angle` | number | 影の方向。度単位です。 |
| `colorIndex` | integer | ファイルのカラーテーブルのインデックスで指定する影の色。 |
| `color` | [色](Common.md#colors) | RGBで指定する影の色（[色](Common.md#colors)を参照）。`color`と`colorIndex`の両方が変更される場合は、`colorIndex`が優先されます。 |
| `opacity` | integer | 不透明度。0～100です。値の範囲はチェックされません。符号なし8ビットの数値として保存されるため、256は0に、-1は255になります。 |
| `byClass` | boolean | オブジェクトのみ: `true`はオブジェクトのクラスのドロップシャドウを使用し、`false`はその使用をやめます。 |
| `delete` | boolean | オブジェクトのみ: オブジェクト自身のドロップシャドウを削除します。 |

オブジェクトに独自のドロップシャドウがない場合、省略したメンバーはVectorworksのデフォルトのドロップシャドウから始まります: `enabled` `false`、`units` `page`、`offset` 0.1、`blurRadius` 0.05、`angle` 315、`colorIndex` ファイル内の黒のインデックス、`opacity` 75。

**例**: オブジェクトから用紙上で0.05インチ離れた位置に、不透明度50%の柔らかな黒い影を付けます。

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

**この形式を使用する場所**

| ツール | 引数 |
|---|---|
| [`editClass`](DocumentAccess.md#editclass) | `dropShadow` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `dropShadow` |

[`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes)の`dropShadow`には、オブジェクトのドロップシャドウをオン／オフにする`true`または`false`も指定できます。

オブジェクトでは、最初に`byClass`が適用され、次に`delete`またはその他のメンバーが適用されます。`delete`が`true`の場合、オブジェクトのドロップシャドウのデータは削除され、その他のメンバーは適用されません。`applied`には、メンバー（または`true`か`false`）の書き込みに対して`dropShadow`、`byClass`を指定した場合は`dropShadowByClass`、`delete`が`true`の場合は`dropShadowDeleted`が含まれます。`delete`がない場合、メンバーは常に書き込まれます。`byClass`だけを指定した場合も同様で、その場合はメンバーが現在の値で書き込まれ、`applied`には`dropShadow`が含まれます。

[`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes)は、常にすべてのメンバーと`byClass`を返します。独自のドロップシャドウがないオブジェクト（`delete`の後も含む）では、上記のデフォルト値を返します。[`getClasses`](DocumentAccess.md#getclasses)（`detailed`）は、クラスのドロップシャドウを同じ形式で返します。[`getPreferences`](DocumentAccess.md#getpreferences)（`defaultAttributes`）は、ファイルのドロップシャドウをこの形式の`documentDropShadow`として返します。これは読み取り専用で、[`setPreferences`](DocumentAccess.md#setpreferences)では書き込めません。

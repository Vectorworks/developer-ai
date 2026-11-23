[English](../../PythonAPI/v2027.2/ObjectPrimitives.Math.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectPrimitives.Math.md)

# Math — eigenständige 2D- und 3D-Mathematik (`api.Math`)

> **Python-Modul:** `api.Math` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

`api.Math` ist ein Untermodul mit eigenständigen mathematischen Werten, die keine Zeichnung benötigen (Import mit `from api.Math import Point2D` oder Verwendung über `api.Math.Point2D`): Punkte und Vektoren (`Point2D` = `Vector2D`, `Point3D` = `Vector3D`), Transformationen (`Transform2D`, `Transform3D`), Rechtecke (`Rect2D`, `RotatedRect2D`), Linien (`Line2D`, `Line3D`), Ebenen (`Plane3D`), Kreise (`Circle2D`), Kreisbögen (`Arc2D`) und Polygone (`Polygon2D` aus `PolyVertex`-Werten) sowie Hilfsfunktionen und Konstanten.

Alle Winkel werden in Radiant angegeben und gegen den Uhrzeigersinn von der positiven X-Achse aus gemessen. Das Ändern eines zurückgegebenen Werts verändert niemals ein Zeichnungsobjekt: Übergeben Sie den Wert wieder an die Schreibmethode des Objekts.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [Math.Point2D](#mathpoint2d)
  - [Math.Transform2D](#mathtransform2d)
  - [Math.Rect2D](#mathrect2d)
  - [Math.RotatedRect2D](#mathrotatedrect2d)
  - [Math.Line2D](#mathline2d)
    - [Math.Line2D.Intersection](#mathline2dintersection)
  - [Math.Circle2D](#mathcircle2d)
  - [Math.Arc2D](#matharc2d)
  - [Math.PolyVertex](#mathpolyvertex)
  - [Math.Polygon2D](#mathpolygon2d)
    - [Math.Polygon2D.CurveLocation](#mathpolygon2dcurvelocation)
  - [Math.Point3D](#mathpoint3d)
  - [Math.Transform3D](#mathtransform3d)
  - [Math.Line3D](#mathline3d)
  - [Math.Plane3D](#mathplane3d)
- [Aufzählungen](#aufzählungen)
  - [Math.VertexType](#mathvertextype)
  - [Math.OffsetJoin](#mathoffsetjoin)
- [Modulfunktionen](#modulfunktionen)
- [Modulkonstanten](#modulkonstanten)
- [Aliase und implizite Konvertierungen](#aliase-und-implizite-konvertierungen)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`Math.Point2D`](#mathpoint2d) | Klasse |  | 2D-Punkt / -Vektor. |
| [`Math.Transform2D`](#mathtransform2d) | Klasse |  | Affine 2D-Transformation. |
| [`Math.Rect2D`](#mathrect2d) | Klasse |  | Achsenparalleles Rechteck. |
| [`Math.RotatedRect2D`](#mathrotatedrect2d) | Klasse |  | Ein gegebenenfalls gedrehtes Rechteck: eine Ecke, die Richtung der Breitenseite und die beiden Seitenlängen. |
| [`Math.Line2D`](#mathline2d) | Klasse |  | Strecke von `start` nach `end`. |
| [`Math.Line2D.Intersection`](#mathline2dintersection) | Klasse (verschachtelt) |  | Schnittpunkt der Geraden. |
| [`Math.Circle2D`](#mathcircle2d) | Klasse |  | Kreis. |
| [`Math.Arc2D`](#matharc2d) | Klasse |  | Kreisbogen. |
| [`Math.PolyVertex`](#mathpolyvertex) | Klasse |  | Ein Scheitelpunkt eines `Polygon2D`: sein Punkt, Scheitelpunkttyp, Bogenradius (bei Radius-Scheitelpunkten) und die Sichtbarkeit der dort beginnenden Kante. |
| [`Math.Polygon2D`](#mathpolygon2d) | Klasse |  | Scheitelpunktliste eines Polygons oder einer Polylinie. |
| [`Math.Polygon2D.CurveLocation`](#mathpolygon2dcurvelocation) | Klasse (verschachtelt) |  | Punkt und ursprünglicher Segmentparameter auf der temporären NURBS-Darstellung des gekrümmten äußeren Polygonpfads. |
| [`Math.Point3D`](#mathpoint3d) | Klasse |  | Von Python verwalteter 3D-Punkt / -Vektor in Millimetern des Weltkoordinatensystems. |
| [`Math.Transform3D`](#mathtransform3d) | Klasse |  | Von Python verwaltete affine 3D-Matrix, die auf Spaltenvektoren wirkt; A * B wendet zuerst B an. |
| [`Math.Line3D`](#mathline3d) | Klasse |  | Von Python verwaltete 3D-Strecke vom Anfang zum Ende in Millimetern des Weltkoordinatensystems. |
| [`Math.Plane3D`](#mathplane3d) | Klasse |  | Von Python verwaltete orientierte unendliche Ebene mit Einheitsnormalenvektor. |
| [`Math.VertexType`](#mathvertextype) | IntEnum |  | Typ eines Polygon-Scheitelpunkts. |
| [`Math.OffsetJoin`](#mathoffsetjoin) | IntEnum |  | Eckentyp für Parallelkonturen von Polygonen (`Polygon2D.Offset`). |
| [Modulfunktionen](#modulfunktionen) | Funktionen | | `AngleDelta`, `AnglesAreEqual`, `AreEqual`, `Clamp`, `DegToRad`, `IsBetween`, `IsGreater`, `IsLess`, `IsZero`, `Lerp`, `NormalizeAngle`, `NormalizeAngleSigned`, `RadToDeg`, `Sign` |
| [Modulkonstanten](#modulkonstanten) | Konstanten | | `kPi`, `kTwoPi`, `kHalfPi`, `kEpsilon`, `kAngleEpsilon` |

## Klassen

### Math.Point2D

> **Vollständiger Name:** `api.Math.Point2D` · **Erbt von:** `api.Object`

2D-Punkt / -Vektor.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Point2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Point2D(inX: float, inY: float)` | Punkt / Vektor mit den Koordinaten `inX`, `inY`. |
| `Point2D(pt: Point2D)` | Konvertiert einen `api.Point2D`-Wertdatensatz. |
| `Point2D(x=..., y=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Point2D(x=...)`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `FromPolar(length: float, angle: float) -> Math.Point2D` *statisch* | Vektor der Länge `length` in Richtung `angle` (Radiant). |
| `UnitFromAngle(angle: float) -> Math.Point2D` *statisch* | Einheitsvektor in Richtung `angle` (Radiant). |

*Arithmetik*

| Methode | Beschreibung |
|---|---|
| `IsEqual(o: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn beide Koordinaten innerhalb von `tolerance` mit `o` übereinstimmen. |
| `IsZero(tolerance: float = 1e-09) -> bool` | True, wenn die Vektorlänge innerhalb von `tolerance` bei null liegt. |

*Vektoroperationen*

| Methode | Beschreibung |
|---|---|
| `Dot(o: Math.Point2D) -> float` | Skalarprodukt mit `o`. |
| `Cross(o: Math.Point2D) -> float` | Kreuzprodukt mit `o` (die Z-Komponente des 3D-Kreuzprodukts). |
| `LengthSquared() -> float` | Quadrat der Vektorlänge (weniger rechenaufwendig als `Length()`). |
| `Length() -> float` | Länge des Vektors (Abstand vom Ursprung). |
| `Angle() -> float` | Richtungswinkel des Vektors in (-pi, pi]. |
| `Normalized() -> Math.Point2D` | Einheitsvektor in derselben Richtung (ein neuer Wert; ein Nullvektor bleibt unverändert). |
| `Normalize() -> Math.Point2D` | Normiert diesen Vektor direkt auf die Einheitslänge und gibt ihn zurück. |
| `WithLength(length: float) -> Math.Point2D` | Vektor in derselben Richtung mit der Länge `length`. |
| `Perpendicular() -> Math.Point2D` | Der um 90 Grad gegen den Uhrzeigersinn gedrehte Vektor. |
| `PerpendicularCW() -> Math.Point2D` | Der um 90 Grad im Uhrzeigersinn gedrehte Vektor. |
| `Rotated(angle: float) -> Math.Point2D` | Der um `angle` Radiant um den Ursprung gedrehte Vektor. |
| `Rotated(angle: float, center: Math.Point2D) -> Math.Point2D` | Der um `angle` Radiant um `center` gedrehte Punkt. |
| `Scaled(sx: float, sy: float, center: Math.Point2D = Math.Point2D(0.0, 0.0)) -> Math.Point2D` | Der relativ zu `center` um `sx` / `sy` skalierte Punkt. |

*Punktoperationen*

| Methode | Beschreibung |
|---|---|
| `DistanceSquaredTo(o: Math.Point2D) -> float` | Quadrat des Abstands zu `o`. |
| `DistanceTo(o: Math.Point2D) -> float` | Abstand zu `o`. |
| `AngleTo(o: Math.Point2D) -> float` | Richtungswinkel (Radiant) von diesem Punkt zu `o`. |
| `MidPoint(o: Math.Point2D) -> Math.Point2D` | Punkt in der Mitte zwischen diesem Punkt und `o`. |
| `Lerp(o: Math.Point2D, t: float) -> Math.Point2D` | Lineare Interpolation in Richtung `o`: `t` = 0 ergibt diesen Punkt, 1 ergibt `o`. |
| `AngleBetween(o: Math.Point2D) -> float` | Vorzeichenbehafteter Winkel von diesem Vektor zu `o` in (-pi, pi]; positive Werte bedeuten gegen den Uhrzeigersinn. |
| `IsParallel(o: Math.Point2D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Vektoren innerhalb von `angleTolerance` parallel sind (gleiche oder entgegengesetzte Richtung). |
| `IsPerpendicular(o: Math.Point2D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Vektoren innerhalb von `angleTolerance` senkrecht zueinander stehen. |
| `Orientation(a: Math.Point2D, b: Math.Point2D, c: Math.Point2D) -> float` *statisch* | Gibt > 0 zurück, wenn `c` links von der Geraden von `a` nach `b` liegt, < 0 bei Lage rechts davon und 0 bei Kollinearität. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `+` | `__add__(o: Math.Point2D) -> Math.Point2D` | `a + b`: Summe der beiden Werte. |
| `-` | `__sub__(o: Math.Point2D) -> Math.Point2D` | `a - b`: Differenz der beiden Werte. |
| `- (unary)` | `__neg__() -> Math.Point2D` | `-a`: der negierte Wert. |
| `*` | `__mul__(s: float) -> Math.Point2D` | `a * s`: der mit einem Skalar skalierte Wert. |
| `/` | `__truediv__(s: float) -> Math.Point2D` | `a / s`: der durch einen Skalar dividierte Wert. |
| `+=` | `__iadd__(o: Math.Point2D) -> Math.Point2D` | `a += b`: addiert den anderen Wert direkt. |
| `-=` | `__isub__(o: Math.Point2D) -> Math.Point2D` | `a -= b`: subtrahiert den anderen Wert direkt. |
| `*=` | `__imul__(s: float) -> Math.Point2D` | `a *= s`: skaliert den Wert direkt mit einem Skalar. |
| `/=` | `__itruediv__(s: float) -> Math.Point2D` | `a /= s`: dividiert den Wert direkt durch einen Skalar. |
| `==` | `__eq__(o: Math.Point2D) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. Exakter Vergleich; verwenden Sie IsEqual für einen toleranzbasierten Vergleich. |
| `!=` | `__ne__(o: Math.Point2D) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |
| `* (reflected)` | `__rmul__(s: float) -> Math.Point2D` | `s * a`: der mit einem Skalar skalierte Wert. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `x` | `float` | X-Koordinate. |
| `y` | `float` | Y-Koordinate. |

### Math.Transform2D

> **Vollständiger Name:** `api.Math.Transform2D` · **Erbt von:** `api.Object`

Affine 2D-Transformation.

```text
| a  b  tx |   | x |
| c  d  ty | * | y |
| 0  0  1  |   | 1 |
```

Die Verknüpfung 'A * B' wendet zuerst B und dann A an.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Transform2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Transform2D(inA: float, inB: float, inC: float, inD: float, inTx: float, inTy: float)` | Transformation, die (x, y) auf (`inA`*x + `inB`*y + `inTx`, `inC`*x + `inD`*y + `inTy`) abbildet. |
| `Transform2D(a=..., b=..., tx=..., c=..., d=..., ty=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Transform2D(a=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Identity() -> Math.Transform2D` *statisch* | Die identische Transformation. |
| `Translation(dx: float, dy: float) -> Math.Transform2D` *statisch* | Verschiebung um `dx`, `dy`. |
| `Translation(v: Math.Point2D) -> Math.Transform2D` *statisch* | Verschiebung um den Vektor `v`. |
| `Rotation(angle: float) -> Math.Transform2D` *statisch* | Drehung um `angle` Radiant um den Ursprung. |
| `Rotation(angle: float, center: Math.Point2D) -> Math.Transform2D` *statisch* | Drehung um `angle` Radiant um `center`. |
| `Scale(sx: float, sy: float) -> Math.Transform2D` *statisch* | Skalierung um `sx` / `sy` um den Ursprung. |
| `Scale(sx: float, sy: float, center: Math.Point2D) -> Math.Transform2D` *statisch* | Skalierung um `sx` / `sy` um `center`. |
| `Mirror(p1: Math.Point2D, p2: Math.Point2D) -> Math.Transform2D` *statisch* | Spiegelung an der Geraden durch p1 und p2. |
| `FromAxes(origin: Math.Point2D, xAxis: Math.Point2D, yAxis: Math.Point2D) -> Math.Transform2D` *statisch* | Bildet die X-/Y-Einheitsachsen auf `xAxis`/`yAxis` und den Ursprung auf `origin` ab. |
| `Then(next: Math.Transform2D) -> Math.Transform2D` | Die Transformation, die zuerst diese und anschließend `next` anwendet. |
| `Apply(p: Math.Point2D) -> Math.Point2D` | Transformiert den Punkt `p` (einschließlich Verschiebung). |
| `ApplyToVector(v: Math.Point2D) -> Math.Point2D` | Transformiert den Vektor `v` (ohne Verschiebung). |
| `Determinant() -> float` | Determinante des linearen Anteils (bei spiegelnden Transformationen negativ). |
| `IsInvertible(tolerance: float = 1e-09) -> bool` | True, wenn die Determinante innerhalb von `tolerance` nicht null ist. |
| `Inverse() -> Math.Transform2D \| None` | Die inverse Transformation; `None`, wenn sich die Transformation nicht invertieren lässt. |
| `GetTranslation() -> Math.Point2D` | Gibt die Verschiebung zurück. |
| `SetTranslation(v: Math.Point2D) -> None` | Setzt die Verschiebung. |
| `GetRotation() -> float` | Gibt die Drehung zurück (Drehung der X-Achse). |
| `GetScaleX() -> float` | Gibt den Skalierungsfaktor in X-Richtung zurück. |
| `GetScaleY() -> float` | Gibt den Skalierungsfaktor in Y-Richtung zurück (bei Spiegelung negativ). |
| `IsMirrored() -> bool` | True, wenn die Transformation spiegelt (negative Determinante). |
| `IsOrthogonal(tolerance: float = 1e-09) -> bool` | Nur Drehung und gleichmäßige/ungleichmäßige Skalierung entlang der Achsen (keine Scherung). |
| `IsIdentity(tolerance: float = 1e-09) -> bool` | True, wenn die Transformation innerhalb von `tolerance` der identischen Transformation entspricht. |
| `IsEqual(o: Math.Transform2D, tolerance: float = 1e-09) -> bool` | True, wenn alle Koeffizienten innerhalb von `tolerance` mit `o` übereinstimmen. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `*` | `__mul__(o: Math.Transform2D) -> Math.Transform2D` | `A * B`: die verknüpfte Transformation (zuerst wird B angewendet, dann A). |
| `*=` | `__imul__(o: Math.Transform2D) -> Math.Transform2D` | `A *= B`: verknüpft die andere Transformation direkt mit dieser Transformation. |
| `()` | `__call__(p: Math.Point2D) -> Math.Point2D` | `T(p)`: wendet die Transformation auf den Punkt an (entspricht `Apply`). |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `a` | `float` | Zeile 1, Spalte 1 der Matrix. |
| `b` | `float` | Zeile 1, Spalte 2 der Matrix. |
| `tx` | `float` | Verschiebung in X-Richtung. |
| `c` | `float` | Zeile 2, Spalte 1 der Matrix. |
| `d` | `float` | Zeile 2, Spalte 2 der Matrix. |
| `ty` | `float` | Verschiebung in Y-Richtung. |

### Math.Rect2D

> **Vollständiger Name:** `api.Math.Rect2D` · **Erbt von:** `api.Object`

Achsenparalleles Rechteck. Y nimmt nach oben zu: top >= bottom. Ein mit dem Standardkonstruktor erzeugtes Rechteck ist leer; das Hinzufügen von Punkten vergrößert es.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Rect2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Rect2D(inLeft: float, inTop: float, inRight: float, inBottom: float)` | Rechteck mit den angegebenen Seiten (Y nimmt nach oben zu: top >= bottom). |
| `Rect2D(p1: Math.Point2D, p2: Math.Point2D)` | Kleinstes Rechteck, das die beiden Eckpunkte `p1` und `p2` enthält. |
| `Rect2D(left=..., bottom=..., right=..., top=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Rect2D(left=...)`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `FromCenter(center: Math.Point2D, width: float, height: float) -> Math.Rect2D` *statisch* | Rechteck der Größe `width` x `height` mit Mittelpunkt `center`. |
| `IsEmpty() -> bool` | True bei einem leeren Rechteck (noch kein Punkt hinzugefügt). |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | Leer oder mit Breite oder Höhe null. |
| `Width() -> float` | Breite (0 bei einem leeren Rechteck). |
| `Height() -> float` | Höhe (0 bei einem leeren Rechteck). |
| `Area() -> float` | Flächeninhalt. |
| `Perimeter() -> float` | Umfang. |
| `Diagonal() -> float` | Länge der Diagonale. |
| `Center() -> Math.Point2D` | Mittelpunkt. |
| `TopLeft() -> Math.Point2D` | Obere linke Ecke. |
| `TopRight() -> Math.Point2D` | Obere rechte Ecke. |
| `BottomLeft() -> Math.Point2D` | Untere linke Ecke. |
| `BottomRight() -> Math.Point2D` | Untere rechte Ecke. |
| `CenterLeft() -> Math.Point2D` | Mitte der linken Seite. |
| `CenterRight() -> Math.Point2D` | Mitte der rechten Seite. |
| `CenterTop() -> Math.Point2D` | Mitte der oberen Seite. |
| `CenterBottom() -> Math.Point2D` | Mitte der unteren Seite. |
| `Corners() -> tuple[Math.Point2D * 4]` | Die vier Ecken gegen den Uhrzeigersinn, beginnend an der unteren linken Ecke. |
| `FromPoints(points: list[Math.Point2D]) -> Math.Rect2D` *statisch* | Kleinstes Rechteck, das alle `points` enthält (bei einer leeren Liste leer). |

*Vergrößern*

| Methode | Beschreibung |
|---|---|
| `Add(p: Math.Point2D) -> Math.Rect2D` | Vergrößert das Rechteck direkt so, dass es den Punkt `p` enthält, und gibt es zurück. |
| `Add(r: Math.Rect2D) -> Math.Rect2D` | Vergrößert das Rechteck direkt so, dass es das Rechteck `r` enthält, und gibt es zurück. |
| `Union(r: Math.Rect2D) -> Math.Rect2D` | Kleinstes Rechteck, das dieses Rechteck und `r` enthält (ein neuer Wert). |
| `Intersection(r: Math.Rect2D) -> Math.Rect2D` | Überlappung dieses Rechtecks mit `r` (leer, wenn sie sich nicht überlappen). |
| `Inflated(dx: float, dy: float) -> Math.Rect2D` | Vergrößert das Rechteck links und rechts um `dx` sowie oben und unten um `dy` (negative Werte verkleinern es). |
| `Offset(v: Math.Point2D) -> Math.Rect2D` | Das um den Vektor `v` verschobene Rechteck. |
| `Transformed(t: Math.Transform2D) -> Math.Rect2D` | Begrenzungsrechteck der transformierten Ecken. |

*Abfragen*

| Methode | Beschreibung |
|---|---|
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn der Punkt `p` innerhalb des Rechtecks oder auf dessen Rand liegt. |
| `Contains(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | True, wenn das Rechteck `r` vollständig innerhalb dieses Rechtecks liegt. |
| `Intersects(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | True, wenn sich die Rechtecke überlappen oder berühren. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Der `p` nächstgelegene Punkt des Rechtecks (`p` selbst, wenn er innerhalb liegt). |
| `DistanceTo(p: Math.Point2D) -> float` | Abstand von `p` zum Rechteck (im Inneren 0). |
| `IsEqual(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | True, wenn alle vier Seiten innerhalb von `tolerance` mit `r` übereinstimmen. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `left` | `float` | Linke Seite (kleinstes X). |
| `bottom` | `float` | Untere Seite (kleinstes Y). |
| `right` | `float` | Rechte Seite (größtes X). |
| `top` | `float` | Obere Seite (größtes Y). |

### Math.RotatedRect2D

> **Vollständiger Name:** `api.Math.RotatedRect2D` · **Erbt von:** `api.Object`

Ein gegebenenfalls gedrehtes Rechteck: eine Ecke, die Richtung der Breitenseite und die beiden Seitenlängen. So speichert Vectorworks Rechtecke und Radiusrechtecke. Ecken (bei positiver Breite und Höhe gegen den Uhrzeigersinn): origin, origin + dir*width, origin + dir*width + perp*height, origin + perp*height; dabei ist perp der um 90 Grad gegen den Uhrzeigersinn gedrehte Vektor `direction`. Negative Breite oder Höhe erstrecken sich in die entgegengesetzte Richtung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RotatedRect2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `RotatedRect2D(inOrigin: Math.Point2D, inDirection: Math.Point2D, inWidth: float, inHeight: float)` | Rechteck mit der Ecke `inOrigin`, der Richtung der Breitenseite `inDirection` und den Seitenlängen `inWidth`, `inHeight`. |
| `RotatedRect2D(r: Math.Rect2D)` | Ungedrehtes Rechteck, das `r` entspricht. |
| `RotatedRect2D(origin=..., direction=..., width=..., height=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `RotatedRect2D(origin=...)`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `FromCenter(center: Math.Point2D, inWidth: float, inHeight: float, angle: float = 0.0) -> Math.RotatedRect2D` *statisch* | Rechteck der Größe `inWidth` x `inHeight` mit Mittelpunkt `center`, um `angle` Radiant gedreht. |
| `Angle() -> float` | Drehwinkel der Breitenseite (Radiant). |
| `WidthVector() -> Math.Point2D` | Vektor entlang der Breitenseite (`direction * width`). |
| `HeightVector() -> Math.Point2D` | Vektor entlang der Höhenseite (senkrecht zur Breitenseite, Länge `height`). |
| `Area() -> float` | Flächeninhalt. |
| `Perimeter() -> float` | Umfang. |
| `Center() -> Math.Point2D` | Mittelpunkt. |
| `IsAxisAligned(angleTolerance: float = 1e-09) -> bool` | True, wenn das Rechteck nicht gedreht ist (innerhalb von `angleTolerance`). |
| `Corners() -> tuple[Math.Point2D * 4]` | Die vier Ecken: Ursprung, Ursprung + Breitenvektor, gegenüberliegende Ecke, Ursprung + Höhenvektor. |
| `Bounds() -> Math.Rect2D` | Achsenparalleles Begrenzungsrechteck. |

*Lokales Koordinatensystem*

| Methode | Beschreibung |
|---|---|
| `LocalToWorld() -> Math.Transform2D` | X entlang der Breitenseite, Y entlang der Höhenseite, Ursprung bei `origin`. |
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb des Rechtecks oder auf dessen Rand liegt. |
| `Offset(v: Math.Point2D) -> Math.RotatedRect2D` | Das um den Vektor `v` verschobene Rechteck. |
| `Rotated(angle: float, center: Math.Point2D) -> Math.RotatedRect2D` | Das um `angle` Radiant um `center` gedrehte Rechteck. |
| `Normalized() -> Math.RotatedRect2D` | Dasselbe Rechteck, auf positive Breite und Höhe normalisiert. |
| `Transformed(t: Math.Transform2D, tolerance: float = 1e-09) -> Math.RotatedRect2D \| None` | Nur Ähnlichkeitstransformationen (Drehung, Verschiebung, gleichmäßige Skalierung, Spiegelung) erhalten die Rechteckform. |
| `IsEqual(r: Math.RotatedRect2D, tolerance: float = 1e-09) -> bool` | True, wenn die Rechtecke innerhalb von `tolerance` übereinstimmen. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `origin` | `Math.Point2D` | Ecke, an der Breiten- und Höhenseite beginnen. |
| `direction` | `Math.Point2D` | Einheitsvektor entlang der Breitenseite. |
| `width` | `float` | Länge der Breitenseite (negative Werte erstrecken sich in die entgegengesetzte Richtung). |
| `height` | `float` | Länge der Höhenseite (negative Werte erstrecken sich in die entgegengesetzte Richtung). |

### Math.Line2D

> **Vollständiger Name:** `api.Math.Line2D` · **Erbt von:** `api.Object`

Strecke von `start` nach `end`. Methoden mit "Infinite" im Namen behandeln die Strecke als Gerade durch beide Punkte. Der Parameter `t` bildet 0 auf `start` und 1 auf `end` ab.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Line2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Line2D(inStart: Math.Point2D, inEnd: Math.Point2D)` | Strecke von `inStart` nach `inEnd`. |
| `Line2D(x1: float, y1: float, x2: float, y2: float)` | Strecke von (`x1`, `y1`) nach (`x2`, `y2`). |
| `Line2D(start=..., end=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Line2D(start=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `FromPointAngleLength(inStart: Math.Point2D, angle: float, length: float) -> Math.Line2D` *statisch* | Strecke mit Anfang `inStart`, Richtung `angle` (Radiant) und Länge `length`. |
| `Vector() -> Math.Point2D` | Vektor von `start` nach `end`. |
| `Direction() -> Math.Point2D` | Einheitsvektor von `start` in Richtung `end`. |
| `Normal() -> Math.Point2D` | Einheitsnormalenvektor, der nach links von der Strecke zeigt. |
| `Length() -> float` | Länge der Strecke. |
| `LengthSquared() -> float` | Quadrat der Streckenlänge. |
| `Angle() -> float` | Richtungswinkel der Strecke (Radiant von der X-Achse aus). |
| `MidPoint() -> Math.Point2D` | Mitte der Strecke. |
| `PointAt(t: float) -> Math.Point2D` | Punkt beim Parameter `t` (0 = `start`, 1 = `end`; andere Werte extrapolieren). |
| `PointAtDistance(distanceFromStart: float) -> Math.Point2D` | Punkt im Abstand `distanceFromStart` von `start` entlang der Geraden. |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | True, wenn Anfang und Ende innerhalb von `tolerance` zusammenfallen. |
| `Bounds() -> Math.Rect2D` | Begrenzungsrechteck der Strecke. |
| `Reversed() -> Math.Line2D` | Die Strecke mit vertauschten `start` und `end`. |
| `Offset(v: Math.Point2D) -> Math.Line2D` | Die um den Vektor `v` verschobene Strecke. |
| `OffsetParallel(distance: float) -> Math.Line2D` | Parallele Gerade im Abstand `distance` nach links (negativ: nach rechts). |
| `Transformed(t: Math.Transform2D) -> Math.Line2D` | Die durch `t` transformierte Strecke. |
| `Rotated(angle: float, center: Math.Point2D) -> Math.Line2D` | Die um `angle` Radiant um `center` gedrehte Strecke. |
| `WithLength(length: float) -> Math.Line2D` | Verschiebt den Endpunkt entlang der Geraden, sodass die Strecke die angegebene Länge hat. |
| `Extended(atStart: float, atEnd: float) -> Math.Line2D` | Verlängert beide Enden (bei negativen Werten werden sie gekürzt). |
| `ProjectParameter(p: Math.Point2D) -> float` | Parameter der Projektion von `p` auf die Gerade. |
| `ProjectInfinite(p: Math.Point2D) -> Math.Point2D` | Projektion von `p` auf die Gerade. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Der `p` nächstgelegene Punkt der Strecke. |
| `DistanceTo(p: Math.Point2D) -> float` | Abstand von `p` zur Strecke. |
| `DistanceToInfinite(p: Math.Point2D) -> float` | Abstand von `p` zur Geraden. |
| `SignedDistanceToInfinite(p: Math.Point2D) -> float` | Positiv, wenn `p` links von der Geraden liegt. |
| `SideOf(p: Math.Point2D, tolerance: float = 1e-09) -> int` | > 0 links, < 0 rechts, 0 auf der Geraden. |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb von `tolerance` auf der Strecke liegt. |
| `IsPointOnInfinite(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb von `tolerance` auf der Geraden liegt. |
| `Mirror(p: Math.Point2D) -> Math.Point2D` | Spiegelbild von `p` an der Geraden. |
| `IsParallel(o: Math.Line2D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Geraden innerhalb von `angleTolerance` parallel sind. |
| `IsPerpendicular(o: Math.Line2D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Geraden innerhalb von `angleTolerance` senkrecht zueinander stehen. |
| `IsCollinear(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True, wenn beide Strecken auf derselben Geraden liegen (innerhalb von `tolerance`). |
| `IntersectInfinite(o: Math.Line2D) -> Math.Line2D.Intersection \| None` | Schnittpunkt der Geraden durch beide Strecken: der Punkt und die Parameter auf beiden Geraden; `None` bei parallelen Geraden. |
| `Intersect(o: Math.Line2D, tolerance: float = 1e-09) -> Math.Point2D \| None` | Schnittpunkt der beiden Strecken (bei parallelen oder kollinearen Strecken wird kein Punkt zurückgegeben). |
| `Intersects(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True, wenn sich die beiden Strecken schneiden oder berühren. |
| `DistanceTo(o: Math.Line2D) -> float` | Kürzester Abstand zwischen den beiden Strecken. |
| `IsEqual(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True, wenn Anfang und Ende innerhalb von `tolerance` mit `o` übereinstimmen. |
| `IsEqualIgnoreDirection(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True, wenn die Strecken in einer der beiden Richtungen innerhalb von `tolerance` mit `o` übereinstimmen. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `start` | `Math.Point2D` | Anfangspunkt. |
| `end` | `Math.Point2D` | Endpunkt. |

#### Math.Line2D.Intersection

> **Vollständiger Name:** `api.Math.Line2D.Intersection` · **Erbt von:** `api.Object`

Schnittpunkt der Geraden. Gibt den Punkt sowie die Parameter auf dieser Geraden und auf `o` zurück.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Intersection()` | Standardwert (Felder mit ihren Standardwerten). |
| `Intersection(point, t, tOther)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `point` | `Math.Point2D` | Schnittpunkt. |
| `t` | `float` | Parameter auf dieser Geraden. |
| `tOther` | `float` | Parameter auf der anderen Geraden. |

### Math.Circle2D

> **Vollständiger Name:** `api.Math.Circle2D` · **Erbt von:** `api.Object`

Kreis.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Circle2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Circle2D(inCenter: Math.Point2D, inRadius: float)` | Kreis mit Mittelpunkt `inCenter` und Radius `inRadius`. |
| `Circle2D(center=..., radius=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Circle2D(center=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `FromDiameter(p1: Math.Point2D, p2: Math.Point2D) -> Math.Circle2D` *statisch* | Kreis, dessen Durchmesser die Strecke von `p1` nach `p2` ist. |
| `FromThreePoints(p1: Math.Point2D, p2: Math.Point2D, p3: Math.Point2D) -> Math.Circle2D \| None` *statisch* | Kreis durch drei Punkte; leer, wenn die Punkte kollinear sind. |
| `Diameter() -> float` | Durchmesser. |
| `Circumference() -> float` | Kreisumfang. |
| `Area() -> float` | Flächeninhalt. |
| `Bounds() -> Math.Rect2D` | Begrenzungsrechteck. |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | True, wenn der Radius null ist (innerhalb von `tolerance`). |
| `PointAt(angle: float) -> Math.Point2D` | Kreispunkt bei `angle` (Radiant). |
| `AngleOf(p: Math.Point2D) -> float` | Richtungswinkel (Radiant) vom Mittelpunkt zu `p`. |
| `TangentAt(angle: float) -> Math.Point2D` | Einheitstangente bei `angle` gegen den Uhrzeigersinn. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Der `p` nächstgelegene Kreispunkt. |
| `DistanceTo(p: Math.Point2D) -> float` | Abstand von `p` zur Kreislinie. |
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb des Kreises oder auf ihm liegt. |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb von `tolerance` auf der Kreislinie liegt. |
| `Offset(v: Math.Point2D) -> Math.Circle2D` | Der um den Vektor `v` verschobene Kreis. |
| `Rotated(angle: float, c: Math.Point2D) -> Math.Circle2D` | Der um `angle` Radiant um `c` gedrehte Kreis. |
| `Scaled(factor: float, c: Math.Point2D) -> Math.Circle2D` | Der relativ zu `c` mit `factor` skalierte Kreis. |
| `IntersectInfinite(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte mit der Geraden (0, 1 oder 2 Punkte). |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte mit der Strecke. |
| `Intersect(o: Math.Circle2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte mit einem anderen Kreis (bei zusammenfallenden Kreisen werden keine Punkte zurückgegeben). |
| `TangentPoints(p: Math.Point2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Berührpunkte auf dem Kreis für Tangenten durch `p` (keine, wenn `p` im Inneren liegt). |
| `IsEqual(o: Math.Circle2D, tolerance: float = 1e-09) -> bool` | True, wenn Mittelpunkt und Radius innerhalb von `tolerance` mit `o` übereinstimmen. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `center` | `Math.Point2D` | Mittelpunkt. |
| `radius` | `float` | Radius. |

### Math.Arc2D

> **Vollständiger Name:** `api.Math.Arc2D` · **Erbt von:** `api.Object`

Kreisbogen. `sweepAngle` ist bei Bögen gegen den Uhrzeigersinn positiv und bei Bögen im Uhrzeigersinn negativ; |sweepAngle| >= 2*pi entspricht einem Vollkreis.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Arc2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Arc2D(inCenter: Math.Point2D, inRadius: float, inStartAngle: float, inSweepAngle: float)` | Kreisbogen mit dem angegebenen Mittelpunkt, Radius, Anfangswinkel und vorzeichenbehafteten Bogenwinkel (Radiant; ein positiver Bogenwinkel verläuft gegen den Uhrzeigersinn). |
| `Arc2D(circle: Math.Circle2D)` | Vollkreisbogen auf `circle`. |
| `Arc2D(center=..., radius=..., startAngle=..., sweepAngle=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Arc2D(center=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `FromCenterStartEnd(inCenter: Math.Point2D, startPt: Math.Point2D, endPt: Math.Point2D, ccw: bool = True) -> Math.Arc2D` *statisch* | Bogen gegen den Uhrzeigersinn (ccw = `True`) oder im Uhrzeigersinn von `startPt` bis zum Strahl durch `endPt`. |
| `FromThreePoints(startPt: Math.Point2D, midPt: Math.Point2D, endPt: Math.Point2D) -> Math.Arc2D \| None` *statisch* | Bogen mit Anfang `startPt`, durch `midPt` und mit Ende `endPt`; leer, wenn die Punkte kollinear sind. |
| `FromTangent(startPt: Math.Point2D, startTangent: Math.Point2D, endPt: Math.Point2D) -> Math.Arc2D \| None` *statisch* | Bogen ab `startPt` mit der angegebenen Anfangstangentenrichtung und Ende `endPt`. |
| `Circle() -> Math.Circle2D` | Der Vollkreis, auf dem der Bogen liegt. |
| `IsFullCircle(tolerance: float = 1e-09) -> bool` | True, wenn der Bogenwinkel eine volle Umdrehung umfasst (innerhalb von `tolerance`). |
| `IsCounterClockwise() -> bool` | True, wenn der Bogenwinkel positiv ist. |
| `EndAngle() -> float` | Winkel des Endpunkts (Anfangswinkel + Bogenwinkel). |
| `MidAngle() -> float` | Winkel der Bogenmitte. |
| `PointAtAngle(angle: float) -> Math.Point2D` | Punkt auf dem Kreis des Bogens bei `angle` (Radiant). |
| `PointAt(t: float) -> Math.Point2D` | Punkt beim Parameter `t` entlang des Bogens (0 = Anfang, 1 = Ende). |
| `StartPoint() -> Math.Point2D` | Anfangspunkt. |
| `EndPoint() -> Math.Point2D` | Endpunkt. |
| `MidPoint() -> Math.Point2D` | Mittelpunkt des Bogens. |
| `TangentAt(t: float) -> Math.Point2D` | Einheitstangente beim Parameter `t` in Bogenrichtung. |
| `Length() -> float` | Bogenlänge. |
| `Chord() -> Math.Line2D` | Strecke vom Anfangspunkt zum Endpunkt. |
| `ChordLength() -> float` | Länge der Sehne. |
| `Sagitta() -> float` | Abstand von der Sehnenmitte zur Bogenmitte. |
| `SectorArea() -> float` | Flächeninhalt des Kreissektors zwischen Mittelpunkt und Bogen. |
| `SegmentArea() -> float` | Flächeninhalt zwischen dem Bogen und seiner Sehne. |
| `ContainsAngle(angle: float, tolerance: float = 1e-09) -> bool` | Ob der vom Mittelpunkt ausgehende Strahl bei `angle` durch den Bogen verläuft. |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb von `tolerance` auf dem Bogen liegt. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Der `p` nächstgelegene Punkt des Bogens. |
| `DistanceTo(p: Math.Point2D) -> float` | Abstand von `p` zum Bogen. |
| `Bounds() -> Math.Rect2D` | Begrenzungsrechteck der Bogenkurve (ohne Mittelpunkt). |
| `Reversed() -> Math.Arc2D` | Derselbe Bogen mit entgegengesetzter Laufrichtung. |
| `Normalized() -> Math.Arc2D` | Derselbe Bogen mit nicht negativem Bogenwinkel und einem Anfangswinkel in [0, 2*pi). |
| `Offset(v: Math.Point2D) -> Math.Arc2D` | Der um den Vektor `v` verschobene Bogen. |
| `Rotated(angle: float, c: Math.Point2D) -> Math.Arc2D` | Der um `angle` Radiant um `c` gedrehte Bogen. |
| `WithRadius(r: float) -> Math.Arc2D` | Konzentrischer Bogen mit anderem Radius (gleiche Winkel). |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte mit einer Strecke / einem anderen Bogen / einem Kreis. |
| `Intersect(circle: Math.Circle2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte mit einer Strecke / einem anderen Bogen / einem Kreis. |
| `Intersect(o: Math.Arc2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte mit einer Strecke / einem anderen Bogen / einem Kreis. |
| `Tessellate(maxDeviation: float) -> list[Math.Point2D]` | Punkte entlang des Bogens mit einer Sehnenabweichung von höchstens `maxDeviation` (einschließlich beider Enden). |
| `IsEqual(o: Math.Arc2D, tolerance: float = 1e-09) -> bool` | True, wenn die Bögen innerhalb von `tolerance` übereinstimmen. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `center` | `Math.Point2D` | Mittelpunkt. |
| `radius` | `float` | Radius. |
| `startAngle` | `float` | Anfangswinkel (Radiant). |
| `sweepAngle` | `float` | Vorzeichenbehafteter Bogenwinkel (Radiant; positiv bedeutet gegen den Uhrzeigersinn). |

### Math.PolyVertex

> **Vollständiger Name:** `api.Math.PolyVertex` · **Erbt von:** `api.Object`

Ein Scheitelpunkt eines `Polygon2D`: sein Punkt, Scheitelpunkttyp, Bogenradius (bei Radius-Scheitelpunkten) und die Sichtbarkeit der dort beginnenden Kante.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PolyVertex()` | Standardwert (Felder mit ihren Standardwerten). |
| `PolyVertex(pt: Math.Point2D, t: Math.VertexType = Math.VertexType.Corner, radius: float = 0.0, vis: bool = True)` | Scheitelpunkt bei `pt` vom Typ `t` (`radius` bei Radius-Scheitelpunkten; `vis` bezeichnet die Sichtbarkeit der dort beginnenden Kante). |
| `PolyVertex(point=..., type=..., arcRadius=..., visible=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `PolyVertex(point=...)`. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: Math.PolyVertex) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: Math.PolyVertex) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `point` | `Math.Point2D` | Position des Scheitelpunkts. |
| `type` | `Math.VertexType` | Scheitelpunkttyp (Ecke, Bézier, kubisch, Bogen, Radius). |
| `arcRadius` | `float` | Nur für `Math.VertexType.Arc`. |
| `visible` | `bool` | Sichtbarkeit der an diesem Scheitelpunkt beginnenden Kante. |

### Math.Polygon2D

> **Vollständiger Name:** `api.Math.Polygon2D` · **Erbt von:** `api.Object`

Scheitelpunktliste eines Polygons oder einer Polylinie. Außer bei GetCurve.../DivideCurveByCount verwenden Berechnungen die Verbindungen zwischen Scheitelpunkten als gerade Kanten; Kurvenscheitelpunkte (Bézier, kubisch, Bogen, Radius) werden als ihre Kontrollpunkte behandelt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Polygon2D()` | Leeres Polygon. |
| `Polygon2D(points: list[Math.Point2D], closed: bool = True)` | Polygon mit Eckscheitelpunkten bei `points`. |
| `Polygon2D(vertices: list[Math.PolyVertex], closed: bool = True)` | Polygon mit den Scheitelpunkten `vertices`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `FromRect(r: Math.Rect2D) -> Math.Polygon2D` *statisch* | Geschlossenes Polygon mit den vier Ecken von `r`. |
| `FromRotatedRect(r: Math.RotatedRect2D) -> Math.Polygon2D` *statisch* | Geschlossenes Polygon mit den vier Ecken des gedrehten Rechtecks `r`. |
| `FromArc(arc: Math.Arc2D, maxDeviation: float, closeThroughCenter: bool = False) -> Math.Polygon2D` *statisch* | Polygon, das `arc` mit höchstens `maxDeviation` Abstand zwischen Sehnen und Bogen annähert; mit `closeThroughCenter` ist das Polygon ein geschlossener Sektor. |
| `RegularPolygon(center: Math.Point2D, circumradius: float, sides: int, startAngle: float = 0.0) -> Math.Polygon2D` *statisch* | Regelmäßiges Polygon mit `sides` Ecken auf einem Kreis mit Radius `circumradius` um `center`; die erste Ecke liegt bei `startAngle`. |

*Scheitelpunkte*

| Methode | Beschreibung |
|---|---|
| `GetVertexCount() -> int` | Anzahl der Scheitelpunkte. |
| `IsEmpty() -> bool` | True, wenn das Polygon keine Scheitelpunkte hat. |
| `GetVertex(i: int) -> Math.PolyVertex` | Gibt den Scheitelpunkt bei `i` zurück. |
| `GetPoint(i: int) -> Math.Point2D` | Gibt den Punkt bei `i` zurück. |
| `SetPoint(i: int, p: Math.Point2D) -> None` | Setzt den Punkt bei `i`. |
| `GetVertices() -> list[Math.PolyVertex]` | Gibt die Scheitelpunkte zurück. |
| `GetPoints() -> list[Math.Point2D]` | Gibt die Punkte zurück. |
| `AddVertex(v: Math.PolyVertex) -> None` | Hängt den Scheitelpunkt `v` an. |
| `AddVertex(p: Math.Point2D, type: Math.VertexType = Math.VertexType.Corner, arcRadius: float = 0.0) -> None` | Hängt einen Scheitelpunkt bei `p` vom Typ `type` an (`arcRadius` bei Radius-Scheitelpunkten). |
| `InsertVertex(beforeIndex: int, v: Math.PolyVertex) -> None` | Fügt `v` vor dem Scheitelpunkt `beforeIndex` ein (hängt ihn an, wenn der Index hinter dem Ende liegt). |
| `RemoveVertex(i: int) -> None` | Entfernt den Scheitelpunkt `i` (wird bei einem Index außerhalb des Bereichs ignoriert). |
| `Clear() -> None` | Entfernt sämtliche Scheitelpunkte und Aussparungen. |
| `IsClosed() -> bool` | True, wenn das Polygon geschlossen ist. |
| `SetClosed(closed: bool) -> None` | Schaltet *Geschlossen* ein oder aus. |
| `HasCurves() -> bool` | True, wenn ein Scheitelpunkt kein Eckscheitelpunkt ist. |
| `HasHiddenEdges() -> bool` | True, wenn eine Kante unsichtbar ist. |
| `GetHoleCount() -> int` | Anzahl der Aussparungen. |
| `GetHole(i: int) -> Math.Polygon2D` | Gibt die Aussparung bei `i` zurück. |
| `AddHole(hole: Math.Polygon2D) -> None` | Fügt `hole` als Aussparung dieses Polygons hinzu. |
| `ClearHoles() -> None` | Entfernt sämtliche Aussparungen. |
| `GetEdgeCount() -> int` | Kanten. Ein geschlossenes Polygon hat so viele Kanten wie Scheitelpunkte, ein offenes eine weniger. |
| `GetEdge(i: int) -> Math.Line2D` | Gibt das Segment vom Scheitelpunkt `i` zum nächsten Scheitelpunkt zurück; vom letzten Scheitelpunkt führt es zurück zu Scheitelpunkt 0. Bei `i >= GetVertexCount()` wird `IndexError` ausgelöst. Bei einem offenen Polygon gibt `i == GetEdgeCount()` das schließende Segment zurück, obwohl es nicht in der Kantenzahl enthalten ist. |

*Messung*

| Methode | Beschreibung |
|---|---|
| `SignedArea() -> float` | Positiv bei Polygonen gegen den Uhrzeigersinn. |
| `Area() -> float` | Flächeninhalt des Polygons (nicht negativ; zur Orientierung siehe `SignedArea`). |
| `Perimeter() -> float` | Gesamtlänge der geraden Scheitelpunktkanten. |
| `Centroid() -> Math.Point2D` | Flächenschwerpunkt bei geschlossenen Polygonen mit einem Flächeninhalt ungleich null, andernfalls Mittelwert der Scheitelpunkte. |
| `Bounds() -> Math.Rect2D` | Begrenzungsrechteck der Scheitelpunkte. |

*Orientierung*

| Methode | Beschreibung |
|---|---|
| `IsCounterClockwise() -> bool` | True, wenn die Scheitelpunkte gegen den Uhrzeigersinn verlaufen (positiver vorzeichenbehafteter Flächeninhalt). |
| `IsClockwise() -> bool` | True, wenn die Scheitelpunkte im Uhrzeigersinn verlaufen (negativer vorzeichenbehafteter Flächeninhalt). |
| `Reverse() -> Math.Polygon2D` | Kehrt die Reihenfolge der Scheitelpunkte um. Die Kantensichtbarkeit bleibt der jeweiligen Kante zugeordnet. |
| `Reversed() -> Math.Polygon2D` | Kopie des Polygons mit umgekehrter Scheitelpunktreihenfolge. |

*Abfragen*

| Methode | Beschreibung |
|---|---|
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | Enthaltenseinstest nach der Gerade-Ungerade-Regel (der Rand zählt zum Inneren). |
| `IsPointOnBoundary(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True, wenn `p` innerhalb von `tolerance` auf einer Kante liegt. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Der `p` nächstgelegene Punkt der Polygonkontur (gerade Scheitelpunktkanten). |
| `DistanceTo(p: Math.Point2D) -> float` | Abstand von `p` zur Polygonkontur (gerade Scheitelpunktkanten). |
| `GetCurveLength() -> float \| None` | Tatsächlicher gekrümmter ÄUSSERER Pfad, im Gegensatz zu den obigen Abfragen des Kontrollpolygons. Vectorworks verwendet eine temporäre NURBS-Kurve; es werden weder Zeichnungsobjekte eingefügt noch Eingaben geändert. Erfordert wie die booleschen Operationen einen aktiven Zeichnungskontext. Umfasst unsichtbare Kanten und die schließende Kante, jedoch keine Aussparungen. Die Einheiten sind Welteinheiten in der eigenen XY-Ebene des Polygons. Parameter kennzeichnen Segmente der temporären NURBS-Kurve. |
| `GetCurveLocationAtDistance(distance: float) -> Math.Polygon2D.CurveLocation \| None` | Gibt die Kurvenposition im Abstand für `distance` zurück. |
| `GetCurvePointAtDistance(distance: float) -> Math.Point2D \| None` | Gibt den Kurvenpunkt im Abstand für `distance` zurück. |
| `GetCurveTangentAtDistance(distance: float) -> Math.Point2D \| None` | Gibt die Kurventangente im Abstand für `distance` zurück. |
| `GetCurveCurvatureAtDistance(distance: float) -> float \| None` | Gibt die Kurvenkrümmung im Abstand für `distance` zurück. |
| `GetCurveClosestPoint(point: Math.Point2D) -> Math.Polygon2D.CurveLocation \| None` | Gibt den nächstgelegenen Kurvenpunkt für `point` zurück. |
| `GetCurveDistanceTo(point: Math.Point2D) -> float \| None` | Gibt den Abstand von `point` zur Kurve zurück. |
| `DivideCurveByCount(count: int, includeEnd: bool = True) -> list[Math.Point2D] \| None` | Genau count >= 2 Punkte in gleichen Bogenlängenabständen; includeEnd=`False` lässt den letzten Endpunkt bzw. die Naht aus. Die Krümmung ist nicht negativ und an Ecken einseitig; bei Geschwindigkeit null oder ungültigen Argumenten schlägt die Berechnung fehl. Fehler geben `None` zurück, niemals eine unvollständige Liste. Abstände müssen in [0, Kurvenlänge] liegen. |
| `IsConvex() -> bool` | True, wenn das Polygon konvex ist. |
| `IsSelfIntersecting(tolerance: float = 1e-09) -> bool` | Ob sich zwei nicht benachbarte Kanten schneiden. |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Schnittpunkte der Kanten mit einer Strecke. |

*Änderung*

| Methode | Beschreibung |
|---|---|
| `Transform(t: Math.Transform2D) -> Math.Polygon2D` | Transformiert das Polygon direkt mit `t` und gibt es zurück. |
| `Transformed(t: Math.Transform2D) -> Math.Polygon2D` | Mit `t` transformierte Kopie des Polygons. |
| `Offset(d: Math.Point2D) -> Math.Polygon2D` | Verschiebt das Polygon direkt um den Vektor `d` und gibt es zurück. |
| `Offset(distance: float, join: Math.OffsetJoin = Math.OffsetJoin.Miter) -> list[Math.Polygon2D]` | Parallelkonturen des Polygons im Abstand `distance` mit dem Eckentyp `join` als Liste von Polygonen. Löst bei fehlgeschlagener Parallelkonturerzeugung `RuntimeError` aus. |
| `Rotate(angle: float, center: Math.Point2D) -> Math.Polygon2D` | Dreht das Polygon direkt um `angle` Radiant um `center` und gibt es zurück. |
| `RemoveDuplicateVertices(tolerance: float = 1e-09) -> Math.Polygon2D` | Entfernt aufeinanderfolgende zusammenfallende Scheitelpunkte (sowie das schließende Duplikat eines geschlossenen Polygons). |
| `RemoveCollinearVertices(tolerance: float = 1e-09) -> Math.Polygon2D` | Entfernt Scheitelpunkte, die auf der Geraden durch ihre Nachbarn liegen (nur Eckscheitelpunkte). |
| `IsEqual(o: Math.Polygon2D, tolerance: float = 1e-09) -> bool` | True, wenn die Scheitelpunkte innerhalb von `tolerance` mit `o` übereinstimmen. |
| `Union(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Vereinigung mit `other` als Liste von Polygonen. Benötigt eine aktive Zeichnung; löst bei fehlgeschlagener Operation `RuntimeError` aus. |
| `Intersection(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Schnittmenge mit `other` als Liste von Polygonen. Benötigt eine aktive Zeichnung; löst bei fehlgeschlagener Operation `RuntimeError` aus. |
| `Difference(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Dieses Polygon abzüglich `other` als Liste von Polygonen. Benötigt eine aktive Zeichnung; löst bei fehlgeschlagener Operation `RuntimeError` aus. |
| `SymmetricDifference(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Bereiche, die von genau einem der beiden Polygone bedeckt werden, als Liste von Polygonen. Benötigt eine aktive Zeichnung; löst bei fehlgeschlagener Operation `RuntimeError` aus. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `len()` | `__len__() -> int` | `len(a)`: Anzahl der Scheitelpunkte. |
| `[]` | `__getitem__(i: int) -> Math.PolyVertex` | `poly[i]`: der Scheitelpunkt bei `i` (negative Indizes zählen vom Ende; `IndexError` bei einem Index außerhalb des Bereichs). |
| `[] =` | `__setitem__(i: int, vertex: Math.PolyVertex) -> None` | `poly[i] = vertex`: ersetzt den Scheitelpunkt bei `i`. |
| `[] =` | `__setitem__(i: int, point: Math.Point2D) -> None` | `poly[i] = point`: verschiebt den Scheitelpunkt bei `i` nach `point` (behält seinen Typ bei). |
| `repr()` | `__repr__() -> str` | `repr(poly)`: `<api.Math.Polygon2D vertices=N closed=True\|False>`. |

#### Math.Polygon2D.CurveLocation

> **Vollständiger Name:** `api.Math.Polygon2D.CurveLocation` · **Erbt von:** `api.Object`

Punkt und ursprünglicher Segmentparameter auf der temporären NURBS-Darstellung des gekrümmten äußeren Polygonpfads.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `CurveLocation()` | Standardwert (Felder mit ihren Standardwerten). |
| `CurveLocation(point, pieceIndex, parameter)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `point` | `Math.Point2D` | Punkt auf der Kurve. |
| `pieceIndex` | `int` | Index des Kurvensegments. |
| `parameter` | `float` | Parameter auf diesem Segment. |

### Math.Point3D

> **Vollständiger Name:** `api.Math.Point3D` · **Erbt von:** `api.Object`

Von Python verwalteter 3D-Punkt / -Vektor in Millimetern des Weltkoordinatensystems. Vector3D ist derselbe Typ. Erzeugung aus x, y, z, einem Point2D mit optionalem Z oder api.Point3D. `Normalized()` gibt einen Wert zurück; `Normalize()` ändert diesen Wert. Die Normierung des Nullvektors ergibt wieder den Nullvektor. Es ist keine Zeichnung erforderlich.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Point3D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Point3D(inX: float, inY: float, inZ: float)` | Punkt / Vektor mit den Koordinaten `inX`, `inY`, `inZ`. |
| `Point3D(point: Math.Point2D, inZ: float = 0.0)` | Punkt mit X und Y von `point` und Z gleich `inZ`. |
| `Point3D(point: Point3D)` | Konvertiert einen `api.Point3D`-Wertdatensatz. |
| `Point3D(x=..., y=..., z=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Point3D(x=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `IsEqual(other: Math.Point3D, tolerance: float = 1e-09) -> bool` | True, wenn alle Koordinaten innerhalb von `tolerance` mit `other` übereinstimmen. |
| `IsZero(tolerance: float = 1e-09) -> bool` | True, wenn die Vektorlänge innerhalb von `tolerance` bei null liegt. |
| `IsFinite() -> bool` | True, wenn keine Koordinate unendlich oder NaN ist. |
| `Dot(other: Math.Point3D) -> float` | Skalarprodukt mit `other`. |
| `Cross(other: Math.Point3D) -> Math.Point3D` | Kreuzprodukt mit `other`. |
| `LengthSquared() -> float` | Quadrat der Vektorlänge. |
| `Length() -> float` | Länge des Vektors. |
| `Normalized() -> Math.Point3D` | Einheitsvektor in derselben Richtung (ein neuer Wert; ein Nullvektor bleibt unverändert). |
| `Normalize() -> Math.Point3D` | Normiert diesen Vektor direkt auf die Einheitslänge und gibt ihn zurück. |
| `WithLength(length: float) -> Math.Point3D` | Vektor in derselben Richtung mit der Länge `length`. |
| `DistanceSquaredTo(other: Math.Point3D) -> float` | Quadrat des Abstands zu `other`. |
| `DistanceTo(other: Math.Point3D) -> float` | Abstand zu `other`. |
| `MidPoint(other: Math.Point3D) -> Math.Point3D` | Punkt in der Mitte zwischen diesem Punkt und `other`. |
| `Lerp(other: Math.Point3D, parameter: float) -> Math.Point3D` | Lineare Interpolation in Richtung `other`: `parameter` = 0 ergibt diesen Punkt, 1 ergibt `other`. |
| `AngleBetween(other: Math.Point3D) -> float` | Winkel zwischen diesem Vektor und `other` (Radiant, 0 .. pi). |
| `IsParallel(other: Math.Point3D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Vektoren innerhalb von `angleTolerance` parallel sind (gleiche oder entgegengesetzte Richtung). |
| `IsPerpendicular(other: Math.Point3D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Vektoren innerhalb von `angleTolerance` senkrecht zueinander stehen. |
| `XY() -> Math.Point2D` | Die X- und Y-Koordinaten als `Math.Point2D`. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `+` | `__add__(other: Math.Point3D) -> Math.Point3D` | `a + b`: Summe der beiden Werte. |
| `-` | `__sub__(other: Math.Point3D) -> Math.Point3D` | `a - b`: Differenz der beiden Werte. |
| `- (unary)` | `__neg__() -> Math.Point3D` | `-a`: der negierte Wert. |
| `*` | `__mul__(scalar: float) -> Math.Point3D` | `a * s`: der mit einem Skalar skalierte Wert. |
| `/` | `__truediv__(scalar: float) -> Math.Point3D` | `a / s`: der durch einen Skalar dividierte Wert. |
| `+=` | `__iadd__(other: Math.Point3D) -> Math.Point3D` | `a += b`: addiert den anderen Wert direkt. |
| `-=` | `__isub__(other: Math.Point3D) -> Math.Point3D` | `a -= b`: subtrahiert den anderen Wert direkt. |
| `*=` | `__imul__(scalar: float) -> Math.Point3D` | `a *= s`: skaliert den Wert direkt mit einem Skalar. |
| `/=` | `__itruediv__(scalar: float) -> Math.Point3D` | `a /= s`: dividiert den Wert direkt durch einen Skalar. |
| `==` | `__eq__(other: Math.Point3D) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(other: Math.Point3D) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |
| `* (reflected)` | `__rmul__(scalar: float) -> Math.Point3D` | `s * a`: der mit einem Skalar skalierte Wert. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `x` | `float` | X-Koordinate. |
| `y` | `float` | Y-Koordinate. |
| `z` | `float` | Z-Koordinate. |

### Math.Transform3D

> **Vollständiger Name:** `api.Math.Transform3D` · **Erbt von:** `api.Object`

Affine Matrix, die auf Spaltenvektoren wirkt; A * B wendet zuerst B und dann A an. Die implizite letzte Zeile ist (0, 0, 0, 1). Winkel werden nach der Rechte-Hand-Regel in Radiant angegeben.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Transform3D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Transform3D(inA: float, inB: float, inC: float, inD: float, inE: float, inF: float, inG: float, inH: float, inI: float, inTx: float, inTy: float, inTz: float)` | Transformation mit den neun linearen Koeffizienten zeilenweise (`inA` .. `inI`) und der Verschiebung `inTx`, `inTy`, `inTz`. |
| `Transform3D(a=..., b=..., c=..., tx=..., d=..., e=..., f=..., ty=..., g=..., h=..., i=..., tz=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Transform3D(a=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Identity() -> Math.Transform3D` *statisch* | Die identische Transformation. |
| `Translation(dx: float, dy: float, dz: float) -> Math.Transform3D` *statisch* | Verschiebung um `dx`, `dy`, `dz`. |
| `Translation(offset: Math.Point3D) -> Math.Transform3D` *statisch* | Verschiebung um den Vektor `offset`. |
| `Scale(sx: float, sy: float, sz: float) -> Math.Transform3D` *statisch* | Skalierung um `sx`, `sy`, `sz` um den Ursprung. |
| `Scale(sx: float, sy: float, sz: float, center: Math.Point3D) -> Math.Transform3D` *statisch* | Skalierung um `sx`, `sy`, `sz` um `center`. |
| `RotationX(angle: float) -> Math.Transform3D` *statisch* | Drehung um `angle` Radiant um die X-Achse. |
| `RotationY(angle: float) -> Math.Transform3D` *statisch* | Drehung um `angle` Radiant um die Y-Achse. |
| `RotationZ(angle: float) -> Math.Transform3D` *statisch* | Drehung um `angle` Radiant um die Z-Achse. |
| `Rotation(angle: float, axis: Math.Point3D, center: Math.Point3D = Math.Point3D()) -> Math.Transform3D \| None` *statisch* | Drehung um `angle` Radiant um die Achse `axis` durch `center` (Rechte-Hand-Regel); `None` bei einer Nullachse. |
| `Mirror(origin: Math.Point3D, normal: Math.Point3D) -> Math.Transform3D \| None` *statisch* | Spiegelung an der Ebene durch `origin` mit dem Normalenvektor `normal`; `None` bei einem Nullnormalenvektor. |
| `FromAxes(origin: Math.Point3D, xAxis: Math.Point3D, yAxis: Math.Point3D, zAxis: Math.Point3D) -> Math.Transform3D` *statisch* | Transformation, die die Einheitsachsen auf `xAxis`, `yAxis`, `zAxis` und den Ursprung auf `origin` abbildet. |
| `Then(next: Math.Transform3D) -> Math.Transform3D` | Diese Transformation, gefolgt von `next` (entspricht `next * self`). |
| `Apply(point: Math.Point3D) -> Math.Point3D` | Transformiert den Punkt `point` (einschließlich Verschiebung). |
| `ApplyToVector(vector: Math.Point3D) -> Math.Point3D` | Transformiert den Vektor `vector` (ohne Verschiebung). |
| `Determinant() -> float` | Determinante des linearen Anteils (bei spiegelnden Transformationen negativ). |
| `IsInvertible(tolerance: float = 1e-09) -> bool` | True, wenn die Determinante innerhalb von `tolerance` nicht null ist. |
| `Inverse() -> Math.Transform3D \| None` | Die inverse Transformation; `None`, wenn sich die Transformation nicht invertieren lässt. |
| `ApplyToNormal(normal: Math.Point3D) -> Math.Point3D \| None` | Transformiert den Flächennormalenvektor `normal` (invers transponiert, normiert); `None`, wenn sich die Transformation nicht invertieren lässt. |
| `GetTranslation() -> Math.Point3D` | Gibt die Verschiebung zurück. |
| `SetTranslation(offset: Math.Point3D) -> None` | Setzt die Verschiebung. |
| `GetXAxis() -> Math.Point3D` | Gibt die X-Achse zurück. |
| `GetYAxis() -> Math.Point3D` | Gibt die Y-Achse zurück. |
| `GetZAxis() -> Math.Point3D` | Gibt die Z-Achse zurück. |
| `IsMirrored() -> bool` | True, wenn die Transformation spiegelt (negative Determinante). |
| `IsOrthogonal(tolerance: float = 1e-09) -> bool` | True, wenn der lineare Anteil eine Drehung oder Spiegelung ohne Skalierung ist (innerhalb von `tolerance`). |
| `IsIdentity(tolerance: float = 1e-09) -> bool` | True, wenn die Transformation innerhalb von `tolerance` der identischen Transformation entspricht. |
| `IsEqual(other: Math.Transform3D, tolerance: float = 1e-09) -> bool` | True, wenn alle Koeffizienten innerhalb von `tolerance` mit `other` übereinstimmen. |
| `IsFinite() -> bool` | True, wenn kein Koeffizient unendlich oder NaN ist. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `*` | `__mul__(other: Math.Transform3D) -> Math.Transform3D` | `A * B`: die verknüpfte Transformation (zuerst wird B angewendet, dann A). |
| `*=` | `__imul__(other: Math.Transform3D) -> Math.Transform3D` | `A *= B`: verknüpft die andere Transformation direkt mit dieser Transformation. |
| `()` | `__call__(point: Math.Point3D) -> Math.Point3D` | `T(p)`: wendet die Transformation auf den Punkt an (entspricht `Apply`). |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `a` | `float` | Zeile 1, Spalte 1 des linearen Anteils. |
| `b` | `float` | Zeile 1, Spalte 2 des linearen Anteils. |
| `c` | `float` | Zeile 1, Spalte 3 des linearen Anteils. |
| `tx` | `float` | Verschiebung in X-Richtung. |
| `d` | `float` | Zeile 2, Spalte 1 des linearen Anteils. |
| `e` | `float` | Zeile 2, Spalte 2 des linearen Anteils. |
| `f` | `float` | Zeile 2, Spalte 3 des linearen Anteils. |
| `ty` | `float` | Verschiebung in Y-Richtung. |
| `g` | `float` | Zeile 3, Spalte 1 des linearen Anteils. |
| `h` | `float` | Zeile 3, Spalte 2 des linearen Anteils. |
| `i` | `float` | Zeile 3, Spalte 3 des linearen Anteils. |
| `tz` | `float` | Verschiebung in Z-Richtung. |

### Math.Line3D

> **Vollständiger Name:** `api.Math.Line3D` · **Erbt von:** `api.Object`

Der Streckenparameter 0 bezeichnet den Anfang und 1 das Ende; Infinite-Methoden begrenzen ihn nicht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Line3D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Line3D(inStart: Math.Point3D, inEnd: Math.Point3D)` | Strecke von `inStart` nach `inEnd`. |
| `Line3D(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float)` | Strecke von (`x1`, `y1`, `z1`) nach (`x2`, `y2`, `z2`). |
| `Line3D(start=..., end=...)` | Feldwerte als Schlüsselwortargumente (beliebige Teilmenge), z. B. `Line3D(start=...)`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Vector() -> Math.Point3D` | Vektor von `start` nach `end`. |
| `Direction() -> Math.Point3D` | Einheitsvektor von `start` in Richtung `end`. |
| `Length() -> float` | Länge der Strecke. |
| `LengthSquared() -> float` | Quadrat der Streckenlänge. |
| `MidPoint() -> Math.Point3D` | Mitte der Strecke. |
| `PointAt(parameter: float) -> Math.Point3D` | Punkt bei `parameter` (0 = `start`, 1 = `end`; andere Werte extrapolieren). |
| `PointAtDistance(distance: float) -> Math.Point3D` | Punkt bei `distance` von `start` aus entlang der Geraden. |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | True, wenn Anfang und Ende innerhalb von `tolerance` zusammenfallen. |
| `Reversed() -> Math.Line3D` | Die Strecke mit vertauschten `start` und `end`. |
| `Offset(offset: Math.Point3D) -> Math.Line3D` | Die um den Vektor `offset` verschobene Strecke. |
| `Transformed(transform: Math.Transform3D) -> Math.Line3D` | Die durch `transform` transformierte Strecke. |
| `WithLength(length: float) -> Math.Line3D` | Strecke mit demselben Anfang und derselben Richtung sowie der Länge `length`. |
| `Extended(atStart: float, atEnd: float) -> Math.Line3D` | Die vor dem Anfang um `atStart` und nach dem Ende um `atEnd` verlängerte Strecke (negative Werte kürzen). |
| `ProjectParameter(point: Math.Point3D) -> float` | Parameter der Projektion von `point` auf die Gerade. |
| `ProjectInfinite(point: Math.Point3D) -> Math.Point3D` | Projektion von `point` auf die Gerade. |
| `ClosestPoint(point: Math.Point3D) -> Math.Point3D` | Der `point` nächstgelegene Punkt der Strecke. |
| `DistanceTo(point: Math.Point3D) -> float` | Abstand von `point` zur Strecke. |
| `DistanceToInfinite(point: Math.Point3D) -> float` | Abstand von `point` zur Geraden. |
| `IsPointOn(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | True, wenn `point` innerhalb von `tolerance` auf der Strecke liegt. |
| `IsPointOnInfinite(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | True, wenn `point` innerhalb von `tolerance` auf der Geraden liegt. |
| `IsParallel(other: Math.Line3D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Geraden innerhalb von `angleTolerance` parallel sind. |
| `IsPerpendicular(other: Math.Line3D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Geraden innerhalb von `angleTolerance` senkrecht zueinander stehen. |
| `IsCollinear(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True, wenn beide Strecken auf derselben Geraden liegen (innerhalb von `tolerance`). |
| `IntersectInfinite(other: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | Schnittpunkt der beiden Geraden; `None`, wenn sie sich nicht treffen (parallel oder windschief). |
| `Intersect(other: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | Schnittpunkt der beiden Strecken; `None`, wenn sie sich nicht in genau einem Punkt treffen. |
| `Intersects(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True, wenn sich die beiden Strecken berühren oder überlappen (einschließlich kollinearer Überlappung). |
| `DistanceTo(other: Math.Line3D) -> float` | Kürzester Abstand zwischen den beiden Strecken. |
| `IsEqual(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True, wenn Anfang und Ende innerhalb von `tolerance` mit `other` übereinstimmen. |
| `IsEqualIgnoreDirection(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True, wenn die Strecken in einer der beiden Richtungen innerhalb von `tolerance` mit `other` übereinstimmen. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `start` | `Math.Point3D` | Anfangspunkt. |
| `end` | `Math.Point3D` | Endpunkt. |

### Math.Plane3D

> **Vollständiger Name:** `api.Math.Plane3D` · **Erbt von:** `api.Object`

Orientierte unendliche Ebene mit Einheitsnormalenvektor. Die Standardebene ist XY mit Normalenvektor +Z.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Plane3D()` | Die XY-Ebene mit Normalenvektor +Z. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `FromPointNormal(origin: Math.Point3D, normal: Math.Point3D) -> Math.Plane3D \| None` *statisch* | Ebene durch `origin` mit Normalenvektor `normal`; `None` bei einem Nullnormalenvektor. |
| `FromPoints(first: Math.Point3D, second: Math.Point3D, third: Math.Point3D) -> Math.Plane3D \| None` *statisch* | Ebene durch drei Punkte (Normalenvektor nach der Rechte-Hand-Regel); `None` bei kollinearen Punkten. |
| `GetOrigin() -> Math.Point3D` | Gibt den Ursprung zurück. |
| `GetNormal() -> Math.Point3D` | Gibt den Normalenvektor zurück. |
| `SignedDistanceTo(point: Math.Point3D) -> float` | Vorzeichenbehafteter Abstand von `point` (positiv auf der Seite, in die der Normalenvektor zeigt). |
| `DistanceTo(point: Math.Point3D) -> float` | Abstand von `point` zur Ebene. |
| `Project(point: Math.Point3D) -> Math.Point3D` | Projektion von `point` auf die Ebene. |
| `Mirror(point: Math.Point3D) -> Math.Point3D` | Spiegelbild von `point` an der Ebene. |
| `Contains(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | True, wenn `point` auf der Ebene liegt (innerhalb von `tolerance`). |
| `Reversed() -> Math.Plane3D` | Dieselbe Ebene mit entgegengesetztem Normalenvektor. |
| `Offset(distance: float) -> Math.Plane3D` | Die um `distance` entlang ihres Normalenvektors verschobene Ebene. |
| `IsParallel(other: Math.Plane3D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Ebenen innerhalb von `angleTolerance` parallel sind. |
| `IsPerpendicular(other: Math.Plane3D, angleTolerance: float = 1e-09) -> bool` | True, wenn die Ebenen innerhalb von `angleTolerance` senkrecht zueinander stehen. |
| `IsEqual(other: Math.Plane3D, tolerance: float = 1e-09, angleTolerance: float = 1e-09) -> bool` | True, wenn die Ebenen innerhalb der Toleranzen zusammenfallen (die Orientierung der Normalenvektoren wird ignoriert). |
| `IntersectInfinite(line: Math.Line3D, angleTolerance: float = 1e-09) -> Math.Point3D \| None` | Schnittpunkt der Geraden durch `line` mit der Ebene; `None` bei Parallelität. |
| `Intersect(line: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | Schnittpunkt der Strecke `line` mit der Ebene; `None`, wenn die Strecke die Ebene nicht kreuzt. |
| `Intersect(other: Math.Plane3D, angleTolerance: float = 1e-09) -> Math.Line3D \| None` | Schnittgerade der beiden Ebenen; `None`, wenn sie parallel sind. |
| `Transformed(transform: Math.Transform3D) -> Math.Plane3D \| None` | Die mit `transform` transformierte Ebene; `None`, wenn sich die Transformation nicht invertieren lässt. |

## Aufzählungen

### Math.VertexType

> **Vollständiger Name:** `api.Math.VertexType` · **Art:** `IntEnum`

Typ eines Polygon-Scheitelpunkts. Die Werte entsprechen den Vectorworks-Konstanten VertexType.

| Element | Wert | Beschreibung |
|---|---|---|
| `Corner` | `0` |  |
| `Bezier` | `1` | Quadratischer Bézier-Kontrollpunkt. |
| `Cubic` | `2` | Kubischer Spline-Kontrollpunkt. |
| `Arc` | `3` | Bogenkontrollpunkt mit Radius (0 = maximaler Radius). |
| `Radius` | `4` | Radius-Kontrollpunkt (tangential). |

### Math.OffsetJoin

> **Vollständiger Name:** `api.Math.OffsetJoin` · **Art:** `IntEnum`

Eckentyp für Parallelkonturen von Polygonen (`Polygon2D.Offset`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Miter` | `0` |  |
| `Round` | `1` |  |

## Modulfunktionen

Funktionen des Moduls `api.Math` (Aufruf als `api.Math.Name(...)`).

| Funktion | Beschreibung |
|---|---|
| `DegToRad(deg: float) -> float` | Wandelt Grad in Radiant um. |
| `RadToDeg(rad: float) -> float` | Wandelt Radiant in Grad um. |
| `IsZero(value: float, tolerance: float = 1e-09) -> bool` | True, wenn `abs(value) <= tolerance`. |
| `AreEqual(a: float, b: float, tolerance: float = 1e-09) -> bool` | True, wenn sich `a` und `b` um höchstens `tolerance` unterscheiden. |
| `IsLess(a: float, b: float, tolerance: float = 1e-09) -> bool` | True, wenn `a < b - tolerance`. |
| `IsGreater(a: float, b: float, tolerance: float = 1e-09) -> bool` | True, wenn `a > b + tolerance`. |
| `IsBetween(v: float, lo: float, hi: float, tolerance: float = 1e-09) -> bool` | True, wenn `v` zwischen `lo` und `hi` liegt (in beliebiger Reihenfolge), mit der Toleranz `tolerance`. |
| `Sign(v: float) -> float` | Vorzeichen von `v`: -1, 0 oder 1. |
| `Clamp(v: float, lo: float, hi: float) -> float` | `v`, begrenzt auf den Bereich `[lo, hi]`. |
| `Lerp(a: float, b: float, t: float) -> float` | Lineare Interpolation: `a + (b - a) * t`. |
| `NormalizeAngle(angle: float) -> float` | Winkel in [0, 2*pi). |
| `NormalizeAngleSigned(angle: float) -> float` | Der auf `(-pi, pi]` normalisierte Winkel. |
| `AngleDelta(from_: float, to: float) -> float` | Winkel gegen den Uhrzeigersinn von `from` nach `to` in [0, 2*pi). |
| `AnglesAreEqual(a: float, b: float, tolerance: float = 1e-09) -> bool` | True, wenn die Winkel `a` und `b` innerhalb von `tolerance` gleich sind (modulo 2*pi). |

## Modulkonstanten

| Konstante | Typ | Wert | Beschreibung |
|---|---|---|---|
| `api.Math.kPi` | `float` | `3.14159265358979323846` | Die Konstante pi. |
| `api.Math.kTwoPi` | `float` | `2.0* `kPi`` | 2 * pi (eine volle Umdrehung in Radiant). |
| `api.Math.kHalfPi` | `float` | `0.5* `kPi`` | pi / 2 (eine Viertelumdrehung in Radiant). |
| `api.Math.kEpsilon` | `float` | `1e-9` | Standard-Abstandstoleranz. |
| `api.Math.kAngleEpsilon` | `float` | `1e-9` | Standard-Winkeltoleranz (Radiant). |

## Aliase und implizite Konvertierungen

- `api.Math.Vector2D` ist ein anderer Name für [`Math.Point2D`](#mathpoint2d) (dasselbe Klassenobjekt).
- `api.Math.Vector3D` ist ein anderer Name für [`Math.Point3D`](#mathpoint3d) (dasselbe Klassenobjekt).
- [`Math.Point2D`](#mathpoint2d) wird als Argument akzeptiert, wenn [`Point2D`](Attributes.md#point2d) erwartet wird (implizite Konvertierung).
- [`Point2D`](Attributes.md#point2d) wird als Argument akzeptiert, wenn [`Math.Point2D`](#mathpoint2d) erwartet wird (implizite Konvertierung).
- [`Math.Point3D`](#mathpoint3d) wird als Argument akzeptiert, wenn [`Point3D`](UIAutomation.md#point3d) erwartet wird (implizite Konvertierung).
- [`Point3D`](UIAutomation.md#point3d) wird als Argument akzeptiert, wenn [`Math.Point3D`](#mathpoint3d) erwartet wird (implizite Konvertierung).

---

[Zurück zum Index](README.md) · [Nach oben](#math--eigenständige-2d--und-3d-mathematik-apimath)

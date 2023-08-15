# RectangleGeom class

This page explains the `RectangleGeom` class.

## What class is this?

The `RectangleGeom` class has the rectangle's geometry interfaces, such as the `left_x`, `center_x`, `right_x`, `top_y`, `center_y`, `bottom_y`, `width`, and `height`.

## Basic usage

In most cases, the apysc initializes the `RectangleGeom` class internally.

For instance, the `get_bounds` method returns a `RectangleGeom` instance; and sets its instance's rectangle geometry data (bounding box).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=200,
    stage_elem_id="stage",
)
rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=200,
    height=75,
    fill_color=ap.Color("#0af"),
)
bounding_box: ap.RectangleGeom = rectangle.get_bounds()
text_1: ap.SVGText = ap.SVGText(
    text=(
        ap.String("Left x: ")
        + bounding_box.left_x.to_string()
        + ap.String(" width: ")
        + bounding_box.width.to_string()
    ),
    x=50,
    y=150,
    fill_color=ap.Color("#aaa"),
)
ap.save_overall_html(dest_dir_path="rectangle_geom_basic_usage/")
```

<iframe src="static/rectangle_geom_basic_usage/index.html" width="300" height="200"></iframe>

## Each attribute point

The following example shows each attribute point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=600,
    stage_height=440,
    stage_elem_id="stage",
)
circle: ap.Circle = ap.Circle(
    x=250,
    y=220,
    radius=150,
    fill_color=ap.Color("#0af"),
)
bounding_box: ap.RectangleGeom = circle.get_bounds()

LINE_COLOR: ap.Color = ap.Color("#aaa")
box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color=LINE_COLOR,
)

POINT_RADIUS: int = 10
fill_color: ap.Color = ap.Color("#fd63c3")
left_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
left_x_and_top_y_text: ap.SVGText = ap.SVGText(
    text="left_x and top_y",
    x=bounding_box.left_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

fill_color = ap.Color("#ae59e3")
right_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.right_x,
    y=bounding_box.top_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
right_x_and_top_y_text: ap.SVGText = ap.SVGText(
    text="right_x and top_y",
    x=bounding_box.right_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

fill_color = ap.Color("#726efa")
left_x_and_bottom_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.bottom_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
left_x_and_bottom_y_text: ap.SVGText = ap.SVGText(
    text="left_x and bottom_y",
    x=bounding_box.left_x,
    y=bounding_box.bottom_y + 31,
    fill_color=fill_color,
)

fill_color = ap.Color("#6eaee6")
right_x_and_bottom_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.right_x,
    y=bounding_box.bottom_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
right_x_and_bottom_y_text: ap.SVGText = ap.SVGText(
    text="right_x and bottom_y",
    x=bounding_box.right_x,
    y=bounding_box.bottom_y + 31,
    fill_color=fill_color,
)

fill_color = ap.Color("#ffffff")
center_x_and_center_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.center_x,
    y=bounding_box.center_y,
    radius=POINT_RADIUS,
    fill_color=fill_color,
)
center_x_and_center_y_text: ap.SVGText = ap.SVGText(
    text="center_x and center_y",
    x=bounding_box.center_x + 25,
    y=bounding_box.center_y + 5,
    fill_color=fill_color,
)

ap.save_overall_html(dest_dir_path="rectangle_geom_each_attribute_point/")
```

<iframe src="static/rectangle_geom_each_attribute_point/index.html" width="600" height="440"></iframe>

## RectangleGeom constructor API

<!-- Docstring: apysc._geom.rectangle_geom.RectangleGeom.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, left_x: apysc._type.number.Number, center_x: apysc._type.number.Number, right_x: apysc._type.number.Number, top_y: apysc._type.number.Number, center_y: apysc._type.number.Number, bottom_y: apysc._type.number.Number, width: apysc._type.int.Int, height: apysc._type.int.Int)`<hr>

**[Interface summary]**

The rectangle's geometry class.<hr>

**[Parameters]**

- `left_x`: Number
  - The rectangle left x coordinate.
- `center_x`: Number
  - The rectangle center x coordinate.
- `right_x`: Number
  - The rectangle right x coordinate.
- `top_y`: Number
  - The rectangle top y coordinate.
- `center_y`: Number
  - The rectangle center y coordinate.
- `bottom_y`: Number
  - The rectangle bottom y coordinate.
- `width`: Int
  - The rectangle width.
- `height`: Int
  - The Rectangle height.

## RectangleGeom left_x property API

<!-- Docstring: apysc._geom.rectangle_geom_left_x_mixin.RectangleGeomLeftXMixIn.left_x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle left x coordinate.<hr>

**[Returns]**

- `left_x`: Number
  - The rectangle left x coordinate.

## RectangleGeom center_x property API

<!-- Docstring: apysc._geom.rectangle_geom_center_x_mixin.RectangleGeomCenterXMixIn.center_x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle center x coordinate.<hr>

**[Returns]**

- `center_x`: Number
  - The rectangle center x coordinate.

## RectangleGeom right_x property API

<!-- Docstring: apysc._geom.rectangle_geom_right_x_mixin.RectangleGeomRightXMixIn.right_x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle right x coordinate.<hr>

**[Returns]**

- `right_x`: Number
  - The rectangle right x coordinate.

## RectangleGeom top_y property API

<!-- Docstring: apysc._geom.rectangle_geom_top_y_mixin.RectangleGeomTopYMixIn.top_y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle top y coordinate.<hr>

**[Returns]**

- `top_y`: Number
  - The rectangle top y coordinate.

## RectangleGeom center_y property API

<!-- Docstring: apysc._geom.rectangle_geom_center_y_mixin.RectangleGeomCenterYMixIn.center_y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle center y coordinate.<hr>

**[Returns]**

- `center_y`: Number
  - The rectangle center y coordinate.

## RectangleGeom bottom_y property API

<!-- Docstring: apysc._geom.rectangle_geom_bottom_y_mixin.RectangleGeomBottomYMixIn.bottom_y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle bottom y coordinate.<hr>

**[Returns]**

- `bottom_y`: Number
  - The rectangle bottom y coordinate.

## RectangleGeom width property API

<!-- Docstring: apysc._geom.rectangle_geom_width_mixin.RectangleGeomWidthMixIn.width -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle geometry width.<hr>

**[Returns]**

- `width`: Int
  - The rectangle geometry width.

## RectangleGeom height property API

<!-- Docstring: apysc._geom.rectangle_geom_height_mixin.RectangleGeomHeightMixIn.height -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get the rectangle geometry height.<hr>

**[Returns]**

- `height`: Int
  - The rectangle geometry height.

## get_bounds method API

<!-- Docstring: apysc._display.get_bounds_mixin.GetBoundsMixIn.get_bounds -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_bounds(self) -> apysc._geom.rectangle_geom.RectangleGeom`<hr>

**[Interface summary]**

Get an instance's bounding-box geometry data.<hr>

**[Returns]**

- `bounding_box`: RectangleGeom
  - An instance's bounding-box geometry data.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage(
...     background_color=ap.Color("#333"), stage_width=250, stage_height=350
... )
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50,
...     y=100,
...     width=150,
...     height=200,
...     fill_color=ap.Color("#0af"),
... )
>>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()
```

<hr>

**[References]**

- [get_bounds interface](https://simon-ritchie.github.io/apysc/en/get_bounds.md)
# get_bounds interface

This page explains the `get_bounds` method interface.

## What interface is this?

The `get_bounds` method returns an instance's bounding box (geometry data, such as the coordinates or size).

## Basic usage

The `get_bounds` method returns a `RectangleGeom` instance.

It does not require any arguments.

Coordinates baseline becomes the stage's x=0 and y=0.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333",
    stage_width=500,
    stage_height=440,
    stage_elem_id="stage",
)
circle: ap.Circle = ap.Circle(
    x=250,
    y=220,
    radius=150,
    fill_color="#0af",
)
bounding_box: ap.RectangleGeom = circle.get_bounds()

LINE_COLOR: str = "#aaa"
box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color="#aaa",
)

fill_color: str = "#fd63c3"
left_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    radius=10,
    fill_color=fill_color,
)
left_x_and_top_y_text: ap.SVGText = ap.SVGText(
    text="left_x and top_y",
    x=bounding_box.left_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

ap.save_overall_html(dest_dir_path="get_bounds_basic_usage/")
```

<iframe src="static/get_bounds_basic_usage/index.html" width="500" height="440"></iframe>

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
...     background_color="#333", stage_width=250, stage_height=350
... )
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50,
...     y=100,
...     width=150,
...     height=200,
...     fill_color="#0af",
... )
>>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()
```

<hr>

**[References]**

- [RectangleGeom class](https://simon-ritchie.github.io/apysc/en/rectangle_geom.html)
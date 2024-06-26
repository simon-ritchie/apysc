# get_bounds interface

This page explains the `get_bounds` method interface.

## What interface is this?

The `get_bounds` method returns an instance's bounding box (geometry data, such as the coordinates or size).

## Basic usage

The `get_bounds` method returns a `RectangleGeom` instance.

This method accepts an optional `target_coordinate_space_object` argument.

If this argument is specified, the reference position of the returned value becomes the relative coordinates from the specified argument's `DisplayObject`.

This is useful when you want to get relative coordinates, such as the coordinates of the parent `DisplayObject`.

If you omit this argument, the reference position becomes the `Stage` coordinates (substantially becoming absolute coordinates).

Example of no argument:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=500,
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

box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color=ap.Color("#aaa"),
)

fill_color: ap.Color = ap.Color("#fd63c3")
left_x_and_top_y_circle: ap.Circle = ap.Circle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    radius=10,
    fill_color=fill_color,
)
left_x_and_top_y_text: ap.SvgText = ap.SvgText(
    text="left_x and top_y",
    x=bounding_box.left_x,
    y=bounding_box.top_y - 15,
    fill_color=fill_color,
)

ap.save_overall_html(dest_dir_path="get_bounds_basic_usage_1/")
```

<iframe src="static/get_bounds_basic_usage_1/index.html" width="500" height="440"></iframe>

Example of using the `target_coordinate_space_object` argument:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=500,
    stage_height=440,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.x = ap.Number(250)
sprite.y = ap.Number(220)
circle: ap.Circle = ap.Circle(
    x=0,
    y=0,
    radius=150,
    fill_color=ap.Color("#0af"),
    parent=sprite,
)
bounding_box: ap.RectangleGeom = circle.get_bounds(
    target_coordinate_space_object=sprite,
)

box_rectangle: ap.Rectangle = ap.Rectangle(
    x=bounding_box.left_x,
    y=bounding_box.top_y,
    width=bounding_box.width,
    height=bounding_box.height,
    line_color=ap.Color("#aaa"),
    parent=sprite,
)

ap.save_overall_html(dest_dir_path="get_bounds_basic_usage_2/")
```

<iframe src="static/get_bounds_basic_usage_2/index.html" width="500" height="440"></iframe>

## get_bounds method API

<!-- Docstring: apysc._display.get_bounds_mixin.GetBoundsMixIn.get_bounds -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_bounds(self, target_coordinate_space_object: Union[apysc._display.display_object.DisplayObject, NoneType] = None) -> apysc._geom.rectangle_geom.RectangleGeom`<hr>

**[Interface summary]**

Get an instance's bounding-box geometry data.<hr>

**[Returns]**

- `bounding_box`: RectangleGeom
  - An instance's bounding-box geometry data.
- `target_coordinate_space_object`: DisplayObject or None, default None
  - Target coordinate space object. If None is specified, then this method returns the bounding-box data based on the stage. If a `DisplayObject` instance is specified, then this method returns the bounding-box data based on the specified object.

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

- [RectangleGeom class](https://simon-ritchie.github.io/apysc/en/rectangle_geom.html)
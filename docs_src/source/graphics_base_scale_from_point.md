# GraphicsBase get_scale_from_point and set_scale_from_point interfaces

This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `get_scale_x_from_point`, `get_scale_y_from_point`, `set_scale_x_from_point`, and `set_scale_y_from_point` method interfaces.

## What interfaces are these?

The `set_scale_x_from_point` method changes the object's horizontal scale from a given x-coordinate. Similarly, the `set_scale_y_from_point` method changes the object's vertical scale from a given y-coordinate.

The `scale_x_from_center` and `scale_y_from_center` interfaces are property, but the `set_scale_x_from_point` and `set_scale_y_from_point` interfaces are methods since these interfaces require a coodinate argument.

Similarly, the `get_scale_x_from_point` and `get_scale_y_from_point` methods will return the current scale from a given point. These interfaces also require a coordinate argument.

Return value is set for each coordinate. For example, if you set the scale-x value at the 50px x-coordinate, 100px x-coordinate scale will not be affected.

## Basic usage

The `get_scale_x_from_point` method requires the `x` argument (`Int` value), and the `set_scale_x_from_point` requires the `scale_x` (`Number` value) and `x` arguments.

The following example creates three rectangles and increments (or decrements) for each rectangle scale-x value. The top rectangle scales from the left x position. The middle one scales from the center x. And the bottom one scales from the right x.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _Options(TypedDict):
    rectangle: ap.Rectangle
    x: ap.Int
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _Options) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    x: ap.Int = options["x"]
    direction: ap.Int = options["direction"]
    current_scale_x: ap.Number = rectangle.get_scale_x_from_point(x=x)
    current_scale_x += direction * 0.03
    rectangle.set_scale_x_from_point(scale_x=current_scale_x, x=x)
    with ap.If(current_scale_x >= 2.0):
        direction *= -1
    with ap.If(current_scale_x <= 0.0):
        direction *= -1


ap.Stage(
    stage_width=150,
    stage_height=350,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))

top_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
middle_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=150, width=50, height=50)
bottom_rect: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=250, width=50, height=50)

top_rect_direction: ap.Int = ap.Int(1)
options: _Options = {
    "rectangle": top_rect,
    "x": ap.Int(50),
    "direction": top_rect_direction,
}
top_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
top_rect_timer.start()

middle_rect_direction: ap.Int = ap.Int(1)
options = {
    "rectangle": middle_rect,
    "x": ap.Int(75),
    "direction": middle_rect_direction,
}
middle_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
middle_rect_timer.start()

bottom_rect_direction: ap.Int = ap.Int(1)
options = {
    "rectangle": bottom_rect,
    "x": ap.Int(100),
    "direction": bottom_rect_direction,
}
bottom_rect_timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
bottom_rect_timer.start()

ap.save_overall_html(dest_dir_path="graphics_base_scale_from_point_basic_usage_x/")
```

<iframe src="static/graphics_base_scale_from_point_basic_usage_x/index.html" width="150" height="350"></iframe>

The `get_scale_y_from_point` and `set_scale_y_from_point` methods have the similar arguments, `scale_y` and `y`. These interfaces work the same way as the x-axis interfaces, except that the axis directions are different.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _Options(TypedDict):
    rectangle: ap.Rectangle
    y: ap.Int
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _Options) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    y: ap.Int = options["y"]
    direction: ap.Int = options["direction"]
    current_scale_y: ap.Number = rectangle.get_scale_y_from_point(y=y)
    current_scale_y += direction * 0.03
    rectangle.set_scale_y_from_point(scale_y=current_scale_y, y=y)
    with ap.If(current_scale_y >= 2.0):
        direction *= -1
    with ap.If(current_scale_y <= 0.0):
        direction *= -1


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
direction: ap.Int = ap.Int(1)
options: _Options = {"rectangle": rectangle, "y": ap.Int(50), "direction": direction}
timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="graphics_base_scale_from_point_basic_usage_y/")
```

<iframe src="static/graphics_base_scale_from_point_basic_usage_y/index.html" width="150" height="150"></iframe>


## get_scale_x_from_point API

<!-- Docstring: apysc._display.scale_x_from_point_mixin.ScaleXFromPointMixIn.get_scale_x_from_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_scale_x_from_point(self, *, x: apysc._type.number.Number) -> apysc._type.number.Number`<hr>

**[Interface summary]**

Get a scale-x value from the given x-coordinate.<hr>

**[Parameters]**

- `x`: Number
  - X-coordinate.

<hr>

**[Returns]**

- `scale_x`: Number
  - Scale-x value from the given x-coordinate.

<hr>

**[Notes]**

The scale's minimum value is almost zero, and it does not become negative.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> x: ap.Number = ap.Number(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

## set_scale_x_from_point API

<!-- Docstring: apysc._display.scale_x_from_point_mixin.ScaleXFromPointMixIn.set_scale_x_from_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `set_scale_x_from_point(self, *, scale_x: apysc._type.number.Number, x: apysc._type.number.Number) -> None`<hr>

**[Interface summary]**

Update a scale-x value from the given x-coordinate.<hr>

**[Parameters]**

- `scale_x`: Number
  - Scale-x value to set.
- `x`: Number
  - X-coordinate.

<hr>

**[Notes]**

The scale's minimum value is almost zero, and it does not become negative.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> x: ap.Number = ap.Number(100)
>>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
>>> rectangle.get_scale_x_from_point(x=x)
Number(1.5)
```

## get_scale_y_from_point API

<!-- Docstring: apysc._display.scale_y_from_point_mixin.ScaleYFromPointMixIn.get_scale_y_from_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_scale_y_from_point(self, *, y: apysc._type.number.Number) -> apysc._type.number.Number`<hr>

**[Interface summary]**

Get a scale-y value from the given y-coordinate.<hr>

**[Parameters]**

- `y`: Number
  - Y-coordinate.

<hr>

**[Returns]**

- `scale_y`: ap.Number
  - Scale-y value from the given y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> y: ap.Number = ap.Number(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```

## set_scale_y_from_point API

<!-- Docstring: apysc._display.scale_y_from_point_mixin.ScaleYFromPointMixIn.set_scale_y_from_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `set_scale_y_from_point(self, *, scale_y: apysc._type.number.Number, y: apysc._type.number.Number) -> None`<hr>

**[Interface summary]**

Update a scale-y value from the given y-coordinate.<hr>

**[Parameters]**

- `scale_y`: Number
  - Scale-y value to set.
- `y`: Number
  - Y-coordinate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> y: ap.Number = ap.Number(100)
>>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
>>> rectangle.get_scale_y_from_point(y=y)
Number(1.5)
```
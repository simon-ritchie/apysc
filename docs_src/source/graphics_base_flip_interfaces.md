# GraphicsBase flip_x and flip_y interfaces

This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `flip_x` and `flip_y` property interfaces.

## What interfaces are these?

The `flip_x` property flips an object in the x-axis direction, and the `flip_y` property flips in the y-axis direction.

## Basic usage

The `flip_x` and `flip_y` can be set a `Boolean` value. If you set the `True`\, an object becomes flipped. Conversely, if you set the `False`\, an object resets flipping.

The getter interface returns a `Boolean` value of a current flipping value.

The following example flips the triangle polygon in the x-axis direction and resets per second:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _PolygonOptions(TypedDict):
    polygon: ap.Polygon


def on_timer(e: ap.TimerEvent, options: _PolygonOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    polygon: ap.Polygon = options['polygon']
    flip_x: ap.Boolean = polygon.flip_x
    flip_x = flip_x.not_
    polygon.flip_x = flip_x


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

polygon: ap.Polygon = sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=75),
    ])
options: _PolygonOptions = {'polygon': polygon}
timer: ap.Timer = ap.Timer(
    on_timer, delay=1000, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_flip_x_basic_usage/')
```

<iframe src="static/graphics_base_flip_x_basic_usage/index.html" width="150" height="150"></iframe>

The `flip_y` interface behaves the same as the `flip_x` interface, except the axis direction.


## flip_x property API

<!-- Docstring: apysc._display.flip_x_interface.FlipXInterface.flip_x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a boolean value whether the x-axis is flipping or not.<hr>

**[Returns]**

- `flip_x`: Boolean
  - A boolean value whether the x-axis is flipping or not.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=25),
...     ])
>>> polygon.flip_x = ap.Boolean(True)
>>> polygon.flip_x
Boolean(True)
```

## flip_y property API

<!-- Docstring: apysc._display.flip_y_interface.FlipYInterface.flip_y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a boolean value whether the y-axis is flipping or not.<hr>

**[Returns]**

- `flip_y`: Boolean
  - A boolean value whether the y-axis is flipping or not.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=0, y=0),
...         ap.Point2D(x=50, y=0),
...         ap.Point2D(x=25, y=50),
...     ])
>>> polygon.flip_y = ap.Boolean(True)
>>> polygon.flip_y
Boolean(True)
```
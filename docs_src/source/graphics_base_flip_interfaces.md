# GraphicsBase flip_x and flip_y interfaces

This page will explain the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `flip_x` and `flip_y` property interfaces.

## What interfaces are these?

The `flip_x` property will flip an object in the x-axis direction, and the `flip_y` property will flip in the y-axis direction.

## Basic usage

The `flip_x` and `flip_y` can be set a `Boolean` value. If you set the `True` then an object will be flipped, conversely, if you set the `False` then an object flipping will be reset.

The getter interface will return a `Boolean` value of a current flipping value.

The following example will flip the triangle polygon in the x-axis direction and reset per second:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _PolygonOptions(TypedDict):
    polygon: ap.Polygon


def on_timer(e: ap.TimerEvent, options: _PolygonOptions) -> None:
    """
    The handler will be called from a timer.

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


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
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

The `flip_y` interface will behave the same as the `flip_x` interface, except the axis direction.

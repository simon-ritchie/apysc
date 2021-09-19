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
from typing import Any
from typing import Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
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
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
sprite.x = ap.Int(100)
sprite.y = ap.Int(50)

polygon: ap.Polygon = sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=0, y=0),
        ap.Point2D(x=0, y=50),
        ap.Point2D(x=50, y=25),
    ])
timer: ap.Timer = ap.Timer(
    on_timer, delay=1000, options={'polygon': polygon})
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_flip_x_basic_usage/')
```

<iframe src="static/graphics_base_flip_x_basic_usage/index.html" width="200" height="150"></iframe>

The `flip_y` interface will behave the same as the `flip_x` interface, except the axis direction.

## Note for coordinates

The coordinates settings (x and y) are also taken into account in the flipping interfaces.

If you don't want to apply the coordinates settings in the flipping interfaces, then set the coordinates to the parent sprite, not a graphics object.

The following example will set no coordinate setting to the first polygon, and also set the 50 y-coordinate to the second polygon and flip in the y-axis direction.

```py
# runnable
from typing import Any
from typing import Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
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
    flip_y: ap.Boolean = polygon.flip_y
    flip_y = flip_y.not_
    polygon.flip_y = flip_y


stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
sprite.x = ap.Int(50)
sprite.y = ap.Int(100)

polygon_1: ap.Polygon = sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=25, y=0),
        ap.Point2D(x=0, y=50),
        ap.Point2D(x=50, y=50),
    ])
timer_1: ap.Timer = ap.Timer(
    on_timer, delay=1000, options={'polygon': polygon_1})
timer_1.start()

polygon_2: ap.Polygon = sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=125, y=0),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=150, y=50),
    ])
polygon_2.y = ap.Int(50)
timer_2: ap.Timer = ap.Timer(
    on_timer, delay=1000, options={'polygon': polygon_2})
timer_2.start()


ap.save_overall_html(
    dest_dir_path='graphics_base_flip_notes/')
```

<iframe src="static/graphics_base_flip_notes/index.html" width="250" height="200"></iframe>

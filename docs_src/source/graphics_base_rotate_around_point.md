# GraphicsBase rotate_around_point interface

This page will explain the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `rotate_around_point` method interface.

## What interface is this?

The `rotate_around_point` method interface will append the rotation angle to its instance (rotate around the specified point).

## Basic usage

The `rotate_around_point` method requires the `additional_rotation`, `x`, and `y` arguments. The `additional_rotation` argument is a value of a rotation degrees to append. The `x` and `y` arguments will determine the rotation coordinates.

The following example will rotate the first rectangle (cyan color rectangle) around the top-left point (`x=50, y=50`), and also rotate the second rectangle (magenta color rectangle) around the bottom-right point (`x=100, y=100`).

```py
# runnable
from typing import Any
from typing import Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from the timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options['rectangle_1']
    rectangle_2: ap.Rectangle = options['rectangle_2']
    rectangle_1.rotate_around_point(additional_rotation=1, x=50, y=50)
    rectangle_2.rotate_around_point(additional_rotation=1, x=100, y=100)


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.begin_fill(color='#0af', alpha=0.5)
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60,
    options={'rectangle_1': rectangle_1, 'rectangle_2': rectangle_2})
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_rotate_around_point_basic_usage/')
```

<iframe src="static/graphics_base_rotate_around_point_basic_usage/index.html" width="150" height="150"></iframe>

## Notes on using the container with relative coordinates

Note that this interface's `x` and `y` coordinates are relative, so if you use the container like the `Sprite` instance, then the container coordinates will be ignored.

The following example will set the container coordinates to `x=50` and `y=50`, and the child rectangle coordinates to `x=0` and `y=0`. The rectangle rotation coordinates are also `x=0` and `y=0` so the rotation point will be the upper-left of the rectangle.

```py
# runnable
from typing import Any
from typing import Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from the timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotate_around_point(additional_rotation=1, x=0, y=0)


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af', alpha=0.5)
sprite.x = ap.Int(50)
sprite.y = ap.Int(50)
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=0, y=0, width=50, height=50)

timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60,
    options={'rectangle': rectangle})
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_rotate_around_point_relative_coord/')
```

<iframe src="static/graphics_base_rotate_around_point_relative_coord/index.html" width="150" height="150"></iframe>

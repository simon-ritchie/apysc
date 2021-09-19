# GraphicsBase skew_x and skew_y interfaces

This page will explain the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `skew_x` and `skew_y` property interfaces.

Each interface value type is the `Int` value.

## What interfaces are these?

The `skew_x` property will skew an object's x-axis, conversely, the `skew_y` property skew a y-axis. These interfaces have getter and setter interfaces.

The following example will show you the default rectangle (left) and the skewed 50px in the x-direction rectangle (right).

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
right_rectangle.skew_x = ap.Int(50)

ap.save_overall_html(
    dest_dir_path='graphics_base_skew_x_basic_usage/')
```

<iframe src="static/graphics_base_skew_x_basic_usage/index.html" width="250" height="150"></iframe>

The following example will skew the rectangle in the y-direction incrementally.

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.skew_y += 1


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60,
    options={'rectangle': rectangle})
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_skew_y_incremental_basic_usage/')
```

<iframe src="static/graphics_base_skew_y_incremental_basic_usage/index.html" width="150" height="150"></iframe>

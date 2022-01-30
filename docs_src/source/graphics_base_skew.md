# GraphicsBase skew_x and skew_y interfaces

This page explains the `GraphicsBase` class (base class of each graphic, such as the `Rectangle`) `skew_x` and `skew_y` property interfaces.

Each interface value type is the `Int` value.

## What interfaces are these?

The `skew_x` property skews an object's x-axis. Conversely, the `skew_y` property skew a y-axis. These interfaces have getter and setter interfaces.

The following example shows you the default rectangle (left) and the skewed 50px in the x-direction rectangle (right).

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
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

The following example skews the rectangle in the y-direction incrementally.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.skew_y += 1


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_skew_y_incremental_basic_usage/')
```

<iframe src="static/graphics_base_skew_y_incremental_basic_usage/index.html" width="150" height="150"></iframe>


## skew_x property API

<!-- Docstring: apysc._display.skew_x_interface.SkewXInterface.skew_x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a current skew x value of the instance.<hr>

**[Returns]**

- `skew_x`: Int
  - Current skew x value of this instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.skew_x = ap.Int(50)
>>> rectangle.skew_x
Int(50)
```

## skew_y property API

<!-- Docstring: apysc._display.skew_y_interface.SkewYInterface.skew_y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a current skew y value of the instance.<hr>

**[Returns]**

- `skew_y`: Int
  - Current skew y value of the instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.skew_y = ap.Int(50)
>>> rectangle.skew_y
Int(50)
```
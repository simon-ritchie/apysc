# GraphicsBase scale_x_from_center and scale_y_from_center interfaces

This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `scale_x_from_center` and `scale_y_from_center` property interfaces.

## What interfaces are these?

The `scale_x_from_center` property changes the object's horizontal scale, and the `scale_y_from_center` property changes the object's vertical scale. These scaling interfaces change the scale from the center coordinates of each object.

## Basic usage

Each property getter interface returns a `Number` value. The setter interfaces also require a `Number` to update scales (If 0.0 is specified, the object becomes invisible. 1.0 becomes the default scale, and 2.0 becomes the twice-scale value).

The following example shows the default scale rectangle (left), horizontally half-scaled rectangle (center), vertically half-scaled rectangle (right).

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
center_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
center_rectangle.scale_x_from_center = ap.Number(0.5)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)
right_rectangle.scale_y_from_center = ap.Number(0.5)

ap.save_overall_html(
    dest_dir_path='graphics_base_scale_from_center_basic_usage_1/')
```

<iframe src="static/graphics_base_scale_from_center_basic_usage_1/index.html" width="350" height="150"></iframe>

These interfaces apply the scaling from the center coordinates, as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af', alpha=0.3)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2.scale_x_from_center = ap.Number(0.5)
rectangle_2.scale_y_from_center = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_3.scale_x_from_center = ap.Number(0.25)
rectangle_3.scale_y_from_center = ap.Number(0.25)

ap.save_overall_html(
    dest_dir_path='graphics_base_scale_from_center_basic_usage_2/')
```

<iframe src="static/graphics_base_scale_from_center_basic_usage_2/index.html" width="150" height="150"></iframe>

The `+=` and `-=` operators are also supported:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectanglesOptions(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle
    direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _RectanglesOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options['rectangle_1']
    rectangle_2: ap.Rectangle = options['rectangle_2']
    direction: ap.Int = options['direction']

    current_scale: ap.Number = rectangle_1.scale_x_from_center
    condition_1: ap.Boolean = current_scale >= 2.0
    condition_2: ap.Boolean = current_scale <= 0.05
    with ap.If(condition_1):
        direction.value = -1
    with ap.Elif(condition_2):
        direction.value = 1

    rectangle_1.scale_x_from_center += direction * 0.03
    rectangle_2.scale_y_from_center += direction * 0.03


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af', alpha=0.5)
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)


direction: ap.Int = ap.Int(1.0)
options: _RectanglesOptions = {
    'rectangle_1': rectangle_1, 'rectangle_2': rectangle_2,
    'direction': direction}
timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60,
    options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_scale_from_center_basic_usage_3/')
```

<iframe src="static/graphics_base_scale_from_center_basic_usage_3/index.html" width="150" height="150"></iframe>


## scale_x_from_center property API

<!-- Docstring: apysc._display.scale_x_from_center_interface.ScaleXFromCenterInterface.scale_x_from_center -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a scale-x value from the center of this instance.<hr>

**[Returns]**

- `scale_x_from_center`: ap.Number
  - Scale-x value from the center of this instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.scale_x_from_center = ap.Number(1.5)
>>> rectangle.scale_x_from_center
Number(1.5)
```

## scale_y_from_center property API

<!-- Docstring: apysc._display.scale_y_from_center_interface.ScaleYFromCenterInterface.scale_y_from_center -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a scale-y value from the center of this instance.<hr>

**[Returns]**

- `scale_y_from_center`: ap.Number
  - Scale-y value from the center of this instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.scale_y_from_center = ap.Number(1.5)
>>> rectangle.scale_y_from_center
Number(1.5)
```
# GraphicsBase rotation_around_point interfaces

This page explains the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `get_rotation_around_point` and `set_rotation_around_point` method interfaces.

## What interfaces are these?

The `get_rotation_around_point` method will return a rotation value around the given coordinates, and the `set_rotation_around_point` method will update a rotation value around the given coordinates.

These rotation values are relative, and each point has the rotation value. For example, the coordinates of the `(x=50, y=50)` and the other coordinates of the `(x=100, y=100)` have different rotation values.

## Basic usage

The `get_rotation_around_point` method requires the `x` and `y` arguments and return a rotation value around the given coordinates. The `set_rotation_around_point` requires `x`, `y` and `rotation` arguments. All the arguments and return value are `Int` type.

The following example creates the two rectangles and rotates each rectangle in the timer handler. The first rectangle rotates around the top-left coordinates (`x=50, y=50`). Also, the second one rotates around the bottom-right coordinates (`x=100, y=100`).

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectanglesOptions(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle


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
    x: ap.Int = ap.Int(50)
    y: ap.Int = ap.Int(50)
    rectangle_1: ap.Rectangle = options['rectangle_1']
    rotation: ap.Int = rectangle_1.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_1.set_rotation_around_point(rotation=rotation, x=x, y=y)

    rectangle_2: ap.Rectangle = options['rectangle_2']
    x = ap.Int(100)
    y = ap.Int(100)
    rotation = rectangle_2.get_rotation_around_point(x=x, y=y)
    rotation += 1
    rectangle_2.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af', alpha=0.5)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectanglesOptions = {
    'rectangle_1': rectangle_1, 'rectangle_2': rectangle_2}
timer: ap.Timer = ap.Timer(
    on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='graphics_base_rotation_around_point_basic_usage/')
```

<iframe src="static/graphics_base_rotation_around_point_basic_usage/index.html" width="150" height="150"></iframe>


## get_rotation_around_point API

<!-- Docstring: apysc._display.rotation_around_point_interface.RotationAroundPointInterface.get_rotation_around_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_rotation_around_point(self, x:apysc._type.int.Int, y:apysc._type.int.Int) -> apysc._type.int.Int`<hr>

**[Interface summary]** Get a rotation value around the given coordinates.<hr>

**[Parameters]**

- `x`: Int
  - X-coordinate.
- `y`: Int
  - Y-coordinate.

<hr>

**[Returns]**

- `rotation`: Int
  - Rotation value around the given coordinates.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> x: ap.Int = ap.Int(100)
>>> y: ap.Int = ap.Int(100)
>>> rectangle.set_rotation_around_point(
...     rotation=ap.Int(45), x=x, y=y)
>>> rectangle.get_rotation_around_point(x=x, y=y)
Int(45)
```

## set_rotation_around_point API

<!-- Docstring: apysc._display.rotation_around_point_interface.RotationAroundPointInterface.set_rotation_around_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `set_rotation_around_point(self, rotation:apysc._type.int.Int, x:apysc._type.int.Int, y:apysc._type.int.Int) -> None`<hr>

**[Interface summary]** Update a rotation value around the given coordinates.<hr>

**[Parameters]**

- `rotation`: Int
  - Rotation value to set.
- `x`: Int
  - X-coordinate.
- `y`: Int
  - Y-coordinate.
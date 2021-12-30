# DisplayObject and GraphicsBase classes base properties abstract

This page would explain the `DisplayObject` and `GraphicsBase` classes' each property (such as the x, visible) abstract.

## What apysc can do in its properties

- You can get/set each property value, such as the x, y, visible, scale, etc.

## x and y properties

The x and y properties can get/set the x and y coordinates.

<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : RectOptions
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    with ap.If(rectangle.x <= 100):
        rectangle.x = rectangle.x + 1
    with ap.Else():
        rectangle.x = rectangle.x - 1

    with ap.If(rectangle.y <= 100):
        rectangle.y = rectangle.y + 1
    with ap.Else():
        rectangle.y = rectangle.y - 1


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: RectOptions = {'rectangle': rectangle}
ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()

ap.save_overall_html(
    dest_dir_path='do_and_graphics_base_prop_abstract_x_and_y/')
```

</details>

<iframe src="static/do_and_graphics_base_prop_abstract_x_and_y/index.html" width="200" height="200"></iframe>

## visible property

## rotation properties

## scale properties

## flip properties

## skew properties

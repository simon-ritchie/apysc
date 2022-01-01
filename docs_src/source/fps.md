# FPS enum

This page explains the `FPS` enum class.

## What class is this?

The `FPS` enum class is the definition of each FPS (frames per second). The timer uses this enum to determine the timer tick interval.

## Basic usage

There is an enum definition of FPS in 5 intervals. The `Timer` class `delay` argument is acceptable `FPS` enum value. For example, specify the `FPS.FPS_60` value to that argument. A timer interval becomes approximately `16.6666667` milliseconds. Similarly, it becomes the `33.3333333` milliseconds when you specify the `FPS.FPS_30` value.

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
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle_1}
timer_1: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_10, options=options)
timer_1.start()

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
options = {'rectangle': rectangle_2}
timer_2: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_30, options=options)
timer_2.start()

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)
options = {'rectangle': rectangle_3}
timer_3: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60, options=options)
timer_3.start()

ap.save_overall_html(
    dest_dir_path='fps_basic_usage/')
```

<iframe src="static/fps_basic_usage/index.html" width="350" height="150"></iframe>

## See also

- [Timer class delay setting](timer_delay.md)

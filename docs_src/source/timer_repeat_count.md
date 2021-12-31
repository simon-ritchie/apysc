# Timer class repeat_count setting

This page will explain the `Timer` class `repeat_count` argument setting.

## What argument is this?

The `repeat_count` argument setting will determine the max handler calling number. If you specify the 10 value, then a timer will call the handler 10 times and will stop.

## Basic usage

You can set the `repeat_count` parameter at the `Timer` constructor. The following example will set the timer with the 100 times `repeat_count` value when you click the rectangle.

If the rectangle was moved 100 times (100-pixels to the right) then the timer will stop.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler would be called when a rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    options_: _RectOptions = {'rectangle': e.this}
    timer: ap.Timer = ap.Timer(
        handler=on_timer, delay=16, repeat_count=100,
        options=options_)
    timer.start()
    e.this.unbind_click(handler=on_rectangle_click)


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.x += 1


ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='timer_repeat_count_basic_usage/')
```

<iframe src="static/timer_repeat_count_basic_usage/index.html" width="250" height="150"></iframe>

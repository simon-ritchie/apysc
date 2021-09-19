# Timer class start and stop interfaces

This page will explain the `Timer` class `start` and `stop` method interfaces.

## What interfaces are these?

The `start` method interface will start a timer. Conversely, the `stop` method interface will stop a timer.

## Basic usage

Each `start` and `stop` method has no arguments. The following example will start the time when you click the rectangle and stop when the timer count is reached 100.

```py
# runnable
from typing import Any, Dict

from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
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
    timer: ap.Timer = e.this
    condition: ap.Boolean = timer.current_count == 100
    with ap.If(condition):
        timer.stop()


stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='timer_start_and_stop_basic_usage/')
```

<iframe src="static/timer_start_and_stop_basic_usage/index.html" width="250" height="150"></iframe>

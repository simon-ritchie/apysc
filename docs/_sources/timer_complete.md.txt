# Timer class timer_complete interface

This page will explain the `Timer` class `timer_complete` method interface.

## What interface is this?

The `timer_complete` method interface will bind a new handler would be called when a timer is complete. For instance, if the `repeat_count` argument is set to 100, then this handler will be called when a timer handling count is reached 100 times.

## Basic usage

The `timer_complete` method has the same interface as the other event binding interface (arguments of the `handler` callable and `options` dictionary).

The following example will start the first timer (rotating the left-side rectangle) when you click the rectangle, and if that one is complete then the second timer will be started:

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_click(e: ap.MouseEvent[ap.Sprite], options: Dict[str, Any]) -> None:
    """
    The handler would be called when any rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click(on_click)
    rectangle_1: ap.Rectangle = options['rectangle_1']
    rectangle_2: ap.Rectangle = options['rectangle_2']
    timer_1: ap.Timer = ap.Timer(
        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90,
        options={'rectangle': rectangle_1})
    timer_1.timer_complete(
        handler=on_timer_1_complete, options={'rectangle_2': rectangle_2})
    timer_1.start()


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
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
    rectangle.rotation_around_center += 1


def on_timer_1_complete(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called when the first timer is complete.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_2: ap.Rectangle = options['rectangle_2']
    timer_2: ap.Timer = ap.Timer(
        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90,
        options={'rectangle': rectangle_2})
    timer_2.start()


stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
sprite.click(
    handler=on_click,
    options={'rectangle_1': rectangle_1, 'rectangle_2': rectangle_2})

ap.save_overall_html(dest_dir_path='timer_complete_basic_usage/')
```

<iframe src="static/timer_complete_basic_usage/index.html" width="250" height="150"></iframe>

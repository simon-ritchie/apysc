# Timer

This page explains the `Timer` class.

## What is the Timer?

The `Timer` class handles the timer's tick. You can call a handler at any intervals by it.

## Basic usage

The `Timer` class requires arguments for the `handler` and `delay` (timer interval in milliseconds). And the `start` method starts that timer. A timer passes the `TimerEvent` instance and options arguments to a specified handler.

The following code sets the `Timer` when clicking the rectangle (`Sprite`):

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click_all()
    timer: ap.Timer = ap.Timer(on_timer, delay=16.6, options=options)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.x += 1


ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='timer_basic_usage/')
```

If you click the rectangle, the timer starts, and the handler increases the rectangle x value.

<iframe src="static/timer_basic_usage/index.html" width="350" height="150"></iframe>

## See also

- [TimerEvent class](timer_event.md)
- [Timer class delay setting](timer_delay.md)
- [FPS enum](fps.md)
- [Timer class repeat count setting](timer_repeat_count.md)
- [Timer class start and stop interfaces](timer_start_and_stop.md)
- [Timer class timer complete interface](timer_complete.md)
- [Timer class reset interface](timer_reset.md)

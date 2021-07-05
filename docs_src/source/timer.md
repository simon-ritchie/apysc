# Timer

This page will explain the `Timer` class.

## What is the Timer

The `Timer` class will handle the timer's tick. You can call a handler at any intervals by it.

## Basic usage

The `Timer` class requires the `handler` and `delay` (timer interval in milliseconds) arguments. And the `start` method will start that timer. A handler would be received a `TimerEvent` instance and options arguments.

The following code will set the `Timer` when the rectangle (`Sprite`) is clicked:

```py
# runnable
from typing import Any, Dict

from apysc import save_overall_html
from apysc import Timer, TimerEvent, MouseEvent
from apysc import Stage, Sprite, Rectangle


def on_sprite_click(
        e: MouseEvent[Sprite], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the sprite is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click_all()
    timer: Timer = Timer(on_timer, delay=16.6, options=options)
    timer.start()


def on_timer(e: TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: Rectangle = options['rectangle']
    rectangle.x += 1


stage: Stage = Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
sprite.click(on_sprite_click, options={'rectangle': rectangle})

save_overall_html(dest_dir_path='timer_basic_usage/')
```

If you click the following rectangle, then the timer will be started, and the rectangle x value will be increased by the timer.

<iframe src="static/timer_basic_usage/index.html" width="350" height="150"></iframe>

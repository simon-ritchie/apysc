# Timer class reset interface

This page explains the `Timer` class `reset` method interface.

## What interface is this?

The `reset` method interface resets a timer count and stops it.

## Basic usage

The `reset` method has no arguments.

The following example rotates the rectangle 90 degrees (`repeat_count=90`) by the first-timer and then reset and start the second one. The second-timer resets and restart the first-timer after 1 second.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


class _TimerOptions(TypedDict):
    timer: ap.Timer


def on_first_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the first-timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.rotation_around_center += 1


def on_first_timer_complete(e: ap.TimerEvent, options: _TimerOptions) -> None:
    """
    The handler that the first-timer calls when completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer_2: ap.Timer = options["timer"]
    timer_2.reset()
    timer_2.start()


def on_second_timer(e: ap.TimerEvent, options: _TimerOptions) -> None:
    """
    The handler that the second timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer_1: ap.Timer = options["timer"]
    timer_1.reset()
    timer_1.start()


options_1: _RectOptions = {"rectangle": rectangle}
timer_1: ap.Timer = ap.Timer(
    handler=on_first_timer, delay=ap.FPS.FPS_60, repeat_count=90, options=options_1
)

options_2: _TimerOptions = {"timer": timer_1}
timer_2: ap.Timer = ap.Timer(
    handler=on_second_timer, delay=1000, repeat_count=1, options=options_2
)
options_2 = {"timer": timer_2}
timer_1.timer_complete(on_first_timer_complete, options=options_2)
timer_1.start()

ap.save_overall_html(dest_dir_path="timer_reset_basic_usage/")
```

<iframe src="static/timer_reset_basic_usage/index.html" width="150" height="150"></iframe>


## reset API

<!-- Docstring: apysc._time.timer.Timer.reset -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `reset(self) -> None`<hr>

**[Interface summary]**

Reset the timer count and stop this timer.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> _ = ap.Stage()
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.x += 1
...     with ap.If(rectangle.x > 100):
...         timer: ap.Timer = e.this
...         timer.reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> options: RectOptions = {"rectangle": rectangle}
>>> _ = ap.Timer(on_timer, delay=33.3, options=options).start()
```
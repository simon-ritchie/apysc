# Timer class start and stop interfaces

This page explains the interface of the Timer class `start` and `stop` methods.

## What interfaces are these?

The `start` method interface starts a timer. Conversely, the `stop` method interface stops a timer.

## Basic usage

Each `start` and `stop` method has no arguments. The following example starts the timer when you click the rectangle and stops when the count reaches 100.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that a rectangle calls when clicked.

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
    The handler what a timer calls.

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


ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='timer_start_and_stop_basic_usage/')
```

<iframe src="static/timer_start_and_stop_basic_usage/index.html" width="250" height="150"></iframe>


## start API

<!-- Docstring: apysc._time.timer.Timer.start -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `start(self) -> None`<hr>

**[Interface summary]** Start this timer.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> _ = ap.Timer(
...     on_timer, delay=33.3, repeat_count=50).start()
```

## stop API

<!-- Docstring: apysc._time.timer.Timer.stop -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `stop(self) -> None`<hr>

**[Interface summary]** Stop this timer.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
...     with ap.If(rectangle.x > 100):
...         timer: ap.Timer = e.this
...         timer.stop()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=33.3, options=options).start()
```
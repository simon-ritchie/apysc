# Timer class repeat_count setting

This page explains the `Timer` class `repeat_count` argument setting.

## What argument is this?

The `repeat_count` argument setting determines the max handler calling number. For example, if you specify the 10 value, a timer calls the handler 10 times and stops.

## Basic usage

You can set the `repeat_count` parameter at the `Timer` constructor. The following example sets the timer with the 100 times `repeat_count` value when clicking the rectangle.

If the timer moves the rectangle 100 times (100-pixels to the right), the timer stops.

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
    The handler that a timer calls.

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


## Timer constructor API

<!-- Docstring: apysc._time.timer.Timer.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, handler:Callable[[_ForwardRef('timer_event.TimerEvent'), ~_O1], NoneType], delay:Union[int, float, apysc._type.number_value_interface.NumberValueInterface, apysc._time.fps.FPS], *, repeat_count:Union[int, apysc._type.int.Int]=0, options:Union[~_O1, NoneType]=None) -> None`<hr>

**[Interface summary]** Timer class to handle function calling at regular intervals.<hr>

**[Parameters]**

- `handler`: _Handler
  - A handler would be called at regular intervals.
- `delay`: Int or int or Number or float or FPS
  - A delay between each `Handler` calling in a millisecond or FPS value. If an `FPS` value is specified, this value becomes a millisecond calculated with that FPS value (e.g., if the `FPS_60` value is specified, then `delay` becomes 16.6666667).
- `repeat_count`: Int or int
  - Max count of a `Handler`'s calling. A timer stops if the `Handler`'s calling count has reached this value. If 0 is specified, then a timer loops forever.
- `options`: dict or None, default None
  - Optional arguments dictionary to pass a `Handler` callable.

<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     rectangle.x += 1
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> _ = ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options).start()
```

<hr>

**[References]**

- [Timer document](https://simon-ritchie.github.io/apysc/timer.html)
- [TimerEvent class document](https://simon-ritchie.github.io/apysc/timer_event.html)
- [Timer class delay setting document](https://simon-ritchie.github.io/apysc/timer_delay.html)
- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## repeat_count property API

<!-- Docstring: apysc._time.timer.Timer.repeat_count -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a max count value of a handler's calling.<hr>

**[Returns]**

- `repeat_count`: Int
  - Max count of a handler's calling. If this value is 0, then a timer loop forever.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> timer: ap.Timer = ap.Timer(
...     on_timer, delay=33.3, repeat_count=50)
>>> timer.repeat_count
Int(50)
```
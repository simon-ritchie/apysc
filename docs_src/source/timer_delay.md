# Timer class delay setting

This page explains the `Timer` class `delay` argument setting.

## What argument is this?

The `delay` argument setting determines the timer tick interval. This setting is a milliseconds unit, so a value of 1000 ticks every 1 second.

The `int`\, `float`\, `Int`\, `Number`\, and `FPS` enum can be acceptable.

## Basic usage

You can set the `delay` parameter at the `Timer` class constructor. The following example sets each timer (`timer_1`, `timer_2`, `timer_3`) and passes the delay values of `100`, `333.3333333`, `16.6666667`.

The first-timer (`delay` is 100) is called 10 times in a second, and the second one (`delay` is 33.3333333) is 30 times in a second, and the third one (`delay` is 16.6666667) is 60 times.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The Handler would be called every timer tick.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


options: _RectOptions = {'rectangle': rectangle_1}
timer_1: ap.Timer = ap.Timer(
    handler=on_timer, delay=100, options=options)
timer_1.start()

options = {'rectangle': rectangle_2}
timer_2: ap.Timer = ap.Timer(
    handler=on_timer, delay=33.3333333, options=options)
timer_2.start()

options = {'rectangle': rectangle_3}
timer_3: ap.Timer = ap.Timer(
    handler=on_timer, delay=16.6666667, options=options)
timer_3.start()

ap.save_overall_html(
    dest_dir_path='timer_delay_basic_usage/')
```

<iframe src="static/timer_delay_basic_usage/index.html" width="350" height="150"></iframe>

## Set the FPS enum value to the delay argument

You can also pass the `FPS` (frames per second) enum value to the `delay` argument. For example, if the `FPS.FPS_60` is specified, a timer delay becomes 60 frames per second (16.6666667 milliseconds). Likely, the `FPS.FPS_30` is specified, a timer delay becomes 30 frames per second (33.3333333 milliseconds).

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The Handler would be called every timer tick.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=ap.FPS.FPS_60,
    options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='timer_delay_fps_enum/')
```

<iframe src="static/timer_delay_fps_enum/index.html" width="150" height="150"></iframe>

## See also

- [FPS enum](fps.md)


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
- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)
- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/timer_repeat_count.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## delay property API

<!-- Docstring: apysc._time.timer.Timer.delay -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a delay value.<hr>

**[Returns]**

- `delay`: Number
  - A delay value of each `Handler` calling in milliseconds.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> timer: ap.Timer = ap.Timer(
...     on_timer, delay=33.3, repeat_count=50)
>>> timer.delay
Number(33.3)
```
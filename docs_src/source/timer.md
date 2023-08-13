# Timer class

This page explains the `Timer` class.

## What is the Timer?

The `Timer` class handles the timer's tick. You can call a handler at any interval by it.

## Basic usage

The `Timer` class requires arguments for the `handler` and `delay` (timer interval in milliseconds). And the `start` method starts that timer. A timer passes the `TimerEvent` instance and options arguments to a specified handler.

The following code sets the `Timer` when clicking the rectangle (`Sprite`):

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:
    """
    The Handler that the rectangle calls when clicked.

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
    The Handler a timer calls.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    rectangle.x += 1


ap.Stage(
    stage_width=350,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _RectOptions = {"rectangle": rectangle}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(dest_dir_path="timer_basic_usage/")
```

If you click the rectangle, the timer starts, and the Handler increases the rectangle x value.

<iframe src="static/timer_basic_usage/index.html" width="350" height="150"></iframe>

## See also

- [TimerEvent class](timer_event.md)
- [Timer class delay setting](timer_delay.md)
- [FPS enum](fps.md)
- [Timer class repeat_count setting](timer_repeat_count.md)
- [Timer class start and stop interfaces](timer_start_and_stop.md)
- [Timer class timer_complete interface](timer_complete.md)
- [Timer class reset interface](timer_reset.md)


## Timer constructor API

<!-- Docstring: apysc._time.timer.Timer.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, handler: Callable[[ForwardRef('TimerEvent'), ~_ConstructorOptions], NoneType], *, delay: Union[int, float, apysc._type.number_value_mixin.NumberValueMixIn, apysc._time.fps.FPS], repeat_count: Union[int, apysc._type.int.Int] = 0, options: Union[~_ConstructorOptions, NoneType] = None) -> None`<hr>

**[Interface summary]**

Timer class to handle function calling at regular intervals.<hr>

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
>>> _ = ap.Stage()
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.x += 1
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> options: RectOptions = {"rectangle": rectangle}
>>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()
```

<hr>

**[References]**

- [TimerEvent class](https://simon-ritchie.github.io/apysc/en/timer_event.html)
- [Timer class delay setting](https://simon-ritchie.github.io/apysc/en/timer_delay.html)
- [FPS enum](https://simon-ritchie.github.io/apysc/en/fps.html)
- [Timer class repeat_count setting](https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html)
- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)
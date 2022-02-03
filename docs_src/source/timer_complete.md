# Timer class timer_complete interface

This page explains the `Timer` class `timer_complete` method interface.

## What interface is this?

The `timer_complete` method interface binds a new handler that a timer calls when it is complete. For instance, if the `repeat_count` argument is 100, it calls this handler when a timer count reaches 100 times.

## Basic usage

The `timer_complete` method has the same interface as the other event binding interface (arguments of the `handler` callable and `options` dictionary).

The following example starts the first timer (rotating the left-side rectangle) when you click the rectangle. If that one completes, then the second timer starts:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectsOptions(TypedDict):
    rectangle_1: ap.Rectangle
    rectangle_2: ap.Rectangle


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_click(e: ap.MouseEvent[ap.Sprite], options: _RectsOptions) -> None:
    """
    The handler that a rectangle calls when clicked.

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
    options_: _RectOptions = {'rectangle': rectangle_1}
    timer_1: ap.Timer = ap.Timer(
        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90,
        options=options_)
    options_ = {'rectangle': rectangle_2}
    timer_1.timer_complete(
        handler=on_timer_1_complete, options=options_)
    timer_1.start()


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
    rectangle.rotation_around_center += 1


def on_timer_1_complete(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the first time calls when completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_2: ap.Rectangle = options['rectangle']
    options_: _RectOptions = {'rectangle': rectangle_2}
    timer_2: ap.Timer = ap.Timer(
        handler=on_timer, delay=ap.FPS.FPS_60, repeat_count=90,
        options=options_)
    timer_2.start()


ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
options: _RectsOptions = {
    'rectangle_1': rectangle_1, 'rectangle_2': rectangle_2}
sprite.click(handler=on_click, options=options)

ap.save_overall_html(
    dest_dir_path='timer_complete_basic_usage/')
```

<iframe src="static/timer_complete_basic_usage/index.html" width="250" height="150"></iframe>


## timer_complete API

<!-- Docstring: apysc._time.timer.Timer.timer_complete -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `timer_complete(self, handler:Callable[[_ForwardRef('timer_event.TimerEvent'), ~_O2], NoneType], *, options:Union[~_O2, NoneType]=None) -> str`<hr>

**[Interface summary]** Add a timer complete event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable that a timer calls when complete.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

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
>>> def on_timer_complete(
...         e: ap.TimerEvent, options: RectOptions) -> None:
...     ap.trace('Timer completed!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> timer: ap.Timer = ap.Timer(
...     on_timer, delay=33.3, options=options)
>>> _ = timer.timer_complete(on_timer_complete)
>>> timer.start()
```

<hr>

**[References]**

- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)
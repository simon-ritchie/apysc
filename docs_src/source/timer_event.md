# TimerEvent class

This page explains the `TimerEvent` class.

## What class is this?

The `TimerEvent` class is the event class that a timer passes to a timer event handler function, such as the `Timer` class constructor or the `timer_complete` function\.

## Basic usage

Each timer event handler's `e` argument becomes the `TimerEvent` class instance.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


def on_timer_complete(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler that the timer calls when completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Timer complete!')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=33.3, options=options)
timer.start()
timer.timer_complete(handler=on_timer_complete)

ap.save_overall_html(
    dest_dir_path='timer_event_basic_usage/')
```

<iframe src="static/timer_event_basic_usage/index.html" width="150" height="150"></iframe>

## This attribute

The `TimerEvent` instance's `this` attribute becomes the target `Timer` instance, and you can use each timer instance interface from it.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1
    ap.trace('Current timer count: ', e.this.current_count)


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=16.6, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='timer_event_this_attribute/')
```

<iframe src="static/timer_event_this_attribute/index.html" width="150" height="150"></iframe>


## TimerEvent constructor API

<!-- Docstring: apysc._event.timer_event.TimerEvent.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, this:'timer.Timer') -> None`<hr>

**[Interface summary]** Timer event class.<hr>

**[Parameters]**

- `this`: Timer
  - Target timer instance.

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
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options,
... ).start()
```

## this attribute API

<!-- Docstring: apysc._event.timer_event.TimerEvent.this -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a timer instance of listening to this event.<hr>

**[Returns]**

- `this`: TImer
  - Instance of listening to this event.

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
...     with ap.If(rectangle.x >= 100):
...         timer: ap.Timer = e.this
...         timer.stop()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60, options=options,
... ).start()
```
# animation_time interface

This page explains the `animation_time` method interface.

## What interface is this?

The `animation_time` interface returns the current animation elapsed time in milliseconds (`Number` type value).

## Basic usage

The following example sets the x-coordinate animation of the rectangle and the 1-second interval timer to display an animation's current elapsed time to console (please press the F12 key).

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the animation calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    ap.trace('Animation elapsed time:', rectangle.animation_time())


ap.Stage(
    stage_width=500, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_x(x=400, duration=10000).start()

options: _RectOptions = {'rectangle': rectangle}
ap.Timer(on_timer, delay=1000, options=options).start()

ap.save_overall_html(
    dest_dir_path='animation_time_basic_usage/')
```

<iframe src="static/animation_time_basic_usage/index.html" width="500" height="150"></iframe>


## animation_time property API

<!-- Docstring: apysc._animation.animation_time_interface.AnimationTimeInterface.animation_time -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_time(self) -> apysc._type.number.Number`<hr>

**[Interface summary]** Get an animation elapsed milisecond.<hr>

**[Returns]**

- `elapsed_time`: Number
  - An animation elapsed millisecond.

<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
>>> def on_timer(
...         e: ap.TimerEvent,
...         options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options['rectangle']
...     animation_time: ap.Number = rectangle.animation_time()
...     ap.trace('animation_time:', animation_time)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {'rectangle': rectangle}
>>> ap.Timer(
...     on_timer, delay=ap.FPS.FPS_60,
...     options=options).start()
```
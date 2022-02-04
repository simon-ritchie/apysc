# animation_finish interface

This page explains the `animation_finish` method interface.

## What interface is this?

The `animation_finish` interface finishes all running animations and sets the last attribute values of each animation setting.

This interface exists in the instances that have the animation interfaces (such as the `animation_x`\, `animation_move`).

## Basic usage

The following example sets the click event to the rectangle. If you click the rectangle, the x-coordinate animation starts. After 2 seconds have passed, the x-coordinate animation finishes and sets the last x-coordinate value of the animation.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.animation_x(
        x=300, duration=5000,
    ).start()

    options_: _RectOptions = {'rectangle': rectangle}
    ap.Timer(
        on_timer, delay=2000, repeat_count=1, options=options_,
    ).start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls when its ends.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.animation_finish()


ap.Stage(
    stage_width=400, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='animation_finish_basic_usage/')
```

<iframe src="static/animation_finish_basic_usage/index.html" width="400" height="150"></iframe>


## animation_finish API

<!-- Docstring: apysc._animation.animation_finish_interface.AnimationFinishInterface.animation_finish -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_finish(self) -> None`<hr>

**[Interface summary]** Finish all animations (set the animation last value to each attribute).<hr>

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
...     rectangle.animation_finish()
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
>>> ap.Timer(on_timer, delay=750, options=options).start()
```
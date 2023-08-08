# animation_reset interface

This page explains the `animation_reset` method interface.

## What interface is this?

The `animation_reset` interface resets all animations and stop.

This interface exists in the instances that have the animation interfaces (such as the `animation_x`\, `animation_move`).

## Basic usage

The following example sets the click event to the rectangle. If you click the rectangle, the x-coordinate animation starts. After 1 second has passed, the `animation_reset` interface resets the x-coordinate animation:

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
    e : ap.Rectangle
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.animation_x(x=500, duration=3000).start()
    options_: _RectOptions = {"rectangle": e.this}
    timer: ap.Timer = ap.Timer(on_timer, delay=1000, repeat_count=1, options=options_)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options["rectangle"].animation_reset()


ap.Stage(
    stage_width=600,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="./animation_reset_basic_usage/")
```

<iframe src="static/animation_reset_basic_usage/index.html" width="600" height=150></iframe>


## animation_reset API

<!-- Docstring: apysc._animation.animation_reset_mixin.AnimationResetMixIn.animation_reset -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_reset(self) -> None`<hr>

**[Interface summary]**

Stop all animations and reset.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_reset()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
>>> options: RectOptions = {"rectangle": rectangle}
>>> ap.Timer(on_timer, delay=750, options=options).start()
```
# animation_pause and animation_play interfaces

This page explains the `animation_pause` and `animation_play` method interfaces.

## What interface are these?

The `animation_pause` interface pauses all the running animations of the target instance. The `animation_play` interface restarts the paused animation.

These interfaces exist in the instances that have the animation interfaces (such as the `animation_x`\, `animation_move`).

## Basic usage

The following example starts the x-coordinate animation and stops after 1 second. After stopping the animation and additionally, 500 milliseconds passed, restarting the animation:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options["rectangle"].animation_pause()
    timer: ap.Timer = ap.Timer(on_timer_2, delay=500, options=options, repeat_count=1)
    timer.start()


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options["rectangle"].animation_play()


ap.Stage(
    stage_width=600,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_x(x=500, duration=15_000).start()

options: _RectOptions = {"rectangle": rectangle}
timer: ap.Timer = ap.Timer(on_timer_1, delay=1000, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="./animation_pause_basic_usage/")
```

<iframe src="static/animation_pause_basic_usage/index.html" width="600" height="150"></iframe>


## animation_pause API

<!-- Docstring: apysc._animation.animation_pause_mixin.AnimationPauseMixIn.animation_pause -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_pause(self) -> None`<hr>

**[Interface summary]**

Stop all animations.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_pause()
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

## animation_play API

<!-- Docstring: apysc._animation.animation_play_mixin.AnimationPlayMixIn.animation_play -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_play(self) -> None`<hr>

**[Interface summary]**

Restart all paused animations.<hr>

**[Examples]**

```py
>>> from typing_extensions import TypedDict
>>> import apysc as ap
>>> class RectOptions(TypedDict):
...     rectangle: ap.Rectangle
...
>>> def on_timer_1(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_pause()
>>> def on_timer_2(e: ap.TimerEvent, options: RectOptions) -> None:
...     rectangle: ap.Rectangle = options["rectangle"]
...     rectangle.animation_play()
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
>>> ap.Timer(on_timer_1, delay=500, options=options).start()
>>> ap.Timer(on_timer_2, delay=1000, options=options).start()
```
# animation_skew_x interface

This page explains the `animation_skew_x` method interface.

## What interface is this?

The `animation_skew_x` method interface creates an `ap.AnimationSkewX` instance. You can animate x-directional skewing with it.

This interface exists on a `GraphicsBase` subclass, such as the `Rectangle`.

## Basic usage

The following example sets the skew-x animation (from 0 to 50) with the `animation_skew_x` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_skew_x(
        skew_x=0,
        duration=DURATION,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_skew_x(
        skew_x=50,
        duration=DURATION,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle.animation_skew_x(
    skew_x=50,
    duration=DURATION,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_skew_x_basic_usage/')
```

<iframe src="static/animation_skew_x_basic_usage/index.html" width="150" height="150"></iframe>

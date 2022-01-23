# animation_fill_alpha interface

This page explains the `animation_fill_alpha` method interface.

## What interface is this?

The `animation_fill_alpha` method interface creates an `ap.AnimationFillAlpha` instance (animation setting instance and the  `AnimationBase` subclass). You can animate fill alpha (opacity) with it.

This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle`.

## Basic usage

The following example sets the fill alpha animation (from 1.0 to 0.0) with the `animation_fill_alpha` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_fill_alpha(
        alpha=1.0, duration=DURATION,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_fill_alpha(
        alpha=0.0, duration=DURATION,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_fill_alpha(
    alpha=0.0, duration=DURATION,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_fill_alpha_basic_usage/')
```

<iframe src="static/animation_fill_alpha_basic_usage/index.html" width="150" height="150"></iframe>
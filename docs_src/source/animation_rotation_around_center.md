# animation_rotation_around_center interface

This page will explain the `animation_rotation_around_center` method interface.

## What interface is this?

The `animation_rotation_around_center` method interface will create an `ap.AnimationRotationAroundCenter` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate rotation around the instance's center point.

This interface exists on a `GraphicsBase` subclass (that has the `rotation_around_center` interface), such as the `Rectangle` or `Circle`.

## Basic usage

The following example will sets the ratation animation (from 0 to 90 degrees) with the `animation_rotation_around_center` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_rotation_around_center(
        rotation_around_center=0,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_rotation_around_center(
        rotation_around_center=90,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_rotation_around_center(
    rotation_around_center=90,
    duration=1000,
    easing=ap.Easing.EASE_OUT_QUINT,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_rotation_around_center_basic_usage/')
```

<iframe src="static/animation_rotation_around_center_basic_usage/index.html" width="150" height="150"></iframe>

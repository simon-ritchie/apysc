# animation_radius interface

This page will explain the `animation_radius` method interface.

## What interface is this?

The `animation_radius` method interface will create an `ap.AnimationRadius` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate radius with it.

This interface exists on a `GraphicsBase` subclass (that has the `radius` interface), such as the `Circle`.

## Basic usage

The following example sets the radius animation (from 50 to 100) with the `animation_radius` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this.target
    circle.animation_radius(
        radius=50, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this.target
    circle.animation_radius(
        radius=100, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=200,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(
    x=100, y=100, radius=50)
circle.animation_radius(
    radius=100, duration=DURATION, easing=ap.Easing.EASE_OUT_QUINT,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_radius_basic_usage/')
```

<iframe src="static/animation_radius_basic_usage/index.html" width="200" height="200"></iframe>

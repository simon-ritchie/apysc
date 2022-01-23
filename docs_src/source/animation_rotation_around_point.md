# animation_rotation_around_point interface

This page explains the `animation_rotation_around_point` method interface.

## What interface is this?

The `animation_rotation_around_point` method interface creates an `ap.AnimationRotationAroundPoint` instance. You can animate rotation around the given point of the instance with it.

This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle`.

## Basic usage

The `animation_rotation_around_point` method requires rotation and x and y coordinates arguments to animate.

The following example sets the rotation animation around the x=100, y=100 coordinates (the bottom-right coordinates of the rectangle) from 0 to 90 degrees.

```py
# runnable
import apysc as ap

DURATION: int = 1000


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
    rectangle.animation_rotation_around_point(
        rotation_around_point=0,
        x=100,
        y=100,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
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
    rectangle.animation_rotation_around_point(
        rotation_around_point=90,
        x=100,
        y=100,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_rotation_around_point(
    rotation_around_point=90,
    x=100,
    y=100,
    duration=1000,
    easing=ap.Easing.EASE_OUT_QUINT,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_rotation_around_point_basic_usage/')
```

<iframe src="static/animation_rotation_around_point_basic_usage/index.html" width="150" height="150"></iframe>
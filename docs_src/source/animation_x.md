# animation_x interface

This page will explain the `animation_x` method interface.

## What interface is this?

The `animation_x` method interface will create an `AnimationX` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate the x-coordinate with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle`.

## Basic usage

The following example sets the x-coordinate animation (from 50 to 100) with the `animation_x` method.

```py
# runnable
import apysc as ap

EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT
DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION, easing=EASING)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=100, duration=DURATION, easing=EASING)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=DURATION, easing=EASING)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_x_basic_usage/')
```

<iframe src="static/animation_x_basic_usage/index.html" width="200" height="150"></iframe>

## Notes for the Circle and Ellipse classes

The `Circle` and `Ellipse` classes' `animation_x` interface will return an `AnimationCx` (center-x) class instance, instead of a `AnimationX` instance, for internal implementation reason.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#00aaff')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
animation_x: ap.AnimationCx = circle.animation_x(
    x=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
```

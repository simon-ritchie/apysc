# animation_width and animation_height interfaces

This page will explain the `animation_width` and `animation_height` interfaces.

## What interfaces are these?

The `animation_width` method interface will create an `AnimationWidth` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate object width with it.

Similarly, the `animation_height` method interface will create an `AnimationHeight` instance and can animate object height with it.

These interfaces exist on some `DisplayObject` instances, such as the `Rectangle`.

## Basic usage

The following example sets the width animation (from 50 to 100) with the `animation_width` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


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
    animation_width: ap.AnimationWidth = rectangle.animation_width(
        width=50, duration=DURATION, easing=EASING)
    animation_width.animation_complete(on_animation_complete_2)
    animation_width.start()


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
    animation_width: ap.AnimationWidth = rectangle.animation_width(
        width=100, duration=DURATION, easing=EASING)
    animation_width.animation_complete(on_animation_complete_1)
    animation_width.start()


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_width: ap.AnimationWidth = rectangle.animation_width(
    width=100, duration=DURATION, easing=EASING)
animation_width.animation_complete(on_animation_complete_1)
animation_width.start()

ap.save_overall_html(
    dest_dir_path='./animation_width_basic_usage/')
```

<iframe src="static/animation_width_basic_usage/index.html" width="200" height="150"></iframe>

Similarly, the following example will animate the height with the `animation_height` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


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
    animation_height: ap.AnimationHeight = rectangle.animation_height(
        height=50, duration=DURATION, easing=EASING)
    animation_height.animation_complete(on_animation_complete_2)
    animation_height.start()


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
    animation_height: ap.AnimationHeight = rectangle.animation_height(
        height=100, duration=DURATION, easing=EASING)
    animation_height.animation_complete(on_animation_complete_1)
    animation_height.start()


ap.Stage(
    stage_width=150, stage_height=200,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_height: ap.AnimationHeight = rectangle.animation_height(
    height=100, duration=DURATION, easing=EASING)
animation_height.animation_complete(on_animation_complete_1)
animation_height.start()

ap.save_overall_html(
    dest_dir_path='./animation_height_basic_usage/')
```

<iframe src="static/animation_height_basic_usage/index.html" width="150" height="200"></iframe>

## Notes for the Ellipse instance

The ellipse instance's `animation_width` and `animation_height` interfaces will return an `AnimationWidthForEllipse` and `AnimationHeightForEllipse` instance instead of an `AnimationWidth` instance, for the reason of the internal implementation, as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=200,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
    x=100, y=100, width=100, height=100)
animation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(
    width=200, duration=1000)
animation_width.start()
```

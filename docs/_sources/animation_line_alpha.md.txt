# animation_line_alpha interface

This page will explain the `animation_line_alpha` method interface.

## What interface is this?

The `animation_line_alpha` method interface will create an `ap.AnimationLineAlpha` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate line alpha (opacity) with it.

This interface exists on a `GraphicsBase` subclass (that has the `line_color` interface), such as the `Rectangle` or `Circle`.

## Basic usage

The following example sets the line alpha animation (from 1.0 to 0.0) with the `animation_line_alpha` method:

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
    rectangle.animation_line_alpha(
        alpha=1.0, duration=DURATION,
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
    rectangle.animation_line_alpha(
        alpha=0.0, duration=DURATION,
    ).animation_complete(on_animation_complete_1).start()


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.line_style(color='#eee', thickness=5, alpha=1.0)
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_line_alpha(
    alpha=0.0, duration=DURATION,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_line_alpha_basic_usage/')
```

<iframe src="static/animation_line_alpha_basic_usage/index.html" width="150" height="150"></iframe>

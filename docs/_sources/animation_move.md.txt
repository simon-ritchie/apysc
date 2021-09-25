# animation_move interface

This page will explain the `animation_move` method interface.

## What interface is this?

The `animation_move` method interface will create an `AnimationMove` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate the x and y coordinates with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle`.

## Basic usage

The following example sets the coordinates animation (from x=50, y=50 to x=100, y=100) with the `animation_move` method.

```py
# runnable
import apysc as ap


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=50, y=50, duration=1000)
    animation_move.animation_complete(on_animation_complete_2)
    animation_move.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=100, y=100, duration=1000)
    animation_move.animation_complete(on_animation_complete_1)
    animation_move.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000)
animation_move.animation_complete(on_animation_complete_1)
animation_move.start()

ap.save_overall_html(
    dest_dir_path='./animation_move_basic_usage/')
```

<iframe src="static/animation_move_basic_usage/index.html" width="200" height="200"></iframe>

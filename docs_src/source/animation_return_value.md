# Each animation interface return value

This page will explain each animation interface, such as the `animation_move`, return value (`AnimationBase` instance).

## Each interface will return the subclass instance of the AnimationBase

Each animation interface will return the subclass instance of the `AnimationBase`. For example, the `animation_move` interface will return the `AnimationMove` instance and the `animation_x` interface will return the `AnimationX` instance.

The `AnimationBase` class has common animation interfaces, such as the `start` (method to start animation), `animation_complete` (method to bind the animation complete event), `target` (property of the animation target).

## Basic usage

Each return value class is in the apysc package (e.g., `ap.AnimationMove`) and you can use it to the type annotation.

The following code example is using the `animation_x` method interface and get an `AnimationX` instance to start and bind the animation complete event with it.

```py
# runnable
import apysc as ap

DURATION: int = 1000


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
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


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
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=100, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=DURATION)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_return_value_basic_usage/')
```

<iframe src="static/animation_return_value_basic_usage/index.html" width="200" height="150"></iframe>

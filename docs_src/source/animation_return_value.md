# Each animation interface return value

This page explains each animation interface, such as the `animation_move`\, return value (`AnimationBase` instance).

## Each interface returns the subclass instance of the AnimationBase

Each animation interface returns the subclass instance of the `AnimationBase`\. So, for example, the `animation_move` interface returns the `AnimationMove` instance, and the `animation_x` interface  returns the `AnimationX` instance.

The `AnimationBase` class has the standard animation interfaces, such as the `start` (method to start animation), `animation_complete` (method to bind the animation completion event), `target` (property of the animation target).

## Basic usage

Each return value class is in the apysc package (e.g., `ap.AnimationMove`). Therefore, you can set the type annotation with it.

The following code example uses the `animation_x` method interface. And You get an `AnimationX` instance to start and bind the animation completion event with it.

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler that the animation calls when its end.

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
    The handler that the animation calls when its end.

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


ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
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
# Animation interfaces delay setting

This page explains the animation interfaces `delay` setting.

## What setting is this?

The `delay` setting determines the delay time before the animation starts. For instance, if you specify 3000 to the `delay` argument, the animation starts after 2 seconds after.

Each animation method interface (such as the `animation_move`\, `animation_x`\, and so on) has the `delay` argument.

## Basic usage

The following example sets 2 seconds between each x-coordinate animation (pause 2 seconds before animation starts):

```py
# runnable
import apysc as ap

DURATION: int = 3000
DELAY: int = 2000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION, delay=DELAY, easing=EASING)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=300, duration=DURATION, delay=DELAY, easing=EASING)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=400, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(
    x=300, duration=DURATION, delay=DELAY, easing=EASING)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_delay_basic_usage/')
```

<iframe src="static/animation_delay_basic_usage/index.html" width="400" height="150"></iframe>

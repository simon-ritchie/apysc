# Animation interfaces duration setting

This page explains the animation interfaces `duration` setting.

## What setting is this?

The `duration` setting determines the animation time from start to end in milliseconds. For instance, if you specify 3000 to the `duration` argument, the animation takes 3 seconds to complete.

Each animation method interface (such as the `animation_move`\, `animation_x`\, and so on) has the `duration` argument.

## Basic usage

The following example sets 3 seconds to the `duration` option and animates x-coordinate.

```py
# runnable
import apysc as ap

DURATION: int = 3000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
        x=50, duration=DURATION, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
        x=400, duration=DURATION, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=500,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(
    x=400, duration=DURATION, easing=EASING
)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(dest_dir_path="./animation_duration_basic_usage/")
```

<iframe src="static/animation_duration_basic_usage/index.html" width="500" height="150"></iframe>
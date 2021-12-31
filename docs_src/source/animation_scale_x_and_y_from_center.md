# animation_scale_x_from_center and animation_scale_x_from_center interfaces

This page will explain the `animation_scale_x_from_center` and `animation_scale_y_from_center` method interfaces.

## What interfaces are these?

The `animation_scale_x_from_center` method interface will create an `ap.AnimationScaleXFromCenter` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate x-directional scale with it.

Similarly, the `animation_scale_y_from_center` method interface will create an `ap.AnimationScaleYFromCenter` instance and you can animate y-directional scale with it.

These interfaces exist on a `GraphicsBase` subclass (that has the `scale_x_from_center` and `scale_y_from_center` interfaces), such as the `Rectangle` or `Circle`.

## Basic usage

The following example sets the scale-x (left-side rectangle) and scale-y (right-side rectangle) animation (from 1.0 to 2.0) with the `animation_scale_x_from_center` and `animation_scale_y_from_center` methods:

```py
# runnable
from enum import Enum

from typing_extensions import TypedDict

import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


class Direction(Enum):
    X = 1
    Y = 2


class Options(TypedDict):
    direction: Direction


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:
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
    SCALE: float = 1.0
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_center(
            scale_x_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_center(
            scale_y_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:
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
    SCALE: float = 2.0
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_center(
            scale_x_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_center(
            scale_y_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()


ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

options: Options = {'direction': Direction.X}
left_rectangle.animation_scale_x_from_center(
    scale_x_from_center=2.0,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

options = {'direction': Direction.Y}
right_rectangle.animation_scale_y_from_center(
    scale_y_from_center=2.0,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

ap.save_overall_html(
    dest_dir_path='./animation_scale_x_and_y_from_center_basic_usage/')
```

<iframe src="static/animation_scale_x_and_y_from_center_basic_usage/index.html" width="250" height="150"></iframe>

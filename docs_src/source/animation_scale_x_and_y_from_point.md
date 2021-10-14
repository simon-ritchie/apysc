# animation_scale_x_from_point and animation_scale_y_from_point interfaces

This page will explain the `animation_scale_x_from_point` and `animation_scale_y_from_point` method interfaces.

## What interfaces are these?

The `animation_scale_x_from_point` method interface will create an `ap.AnimationScaleXFromPoint` instance (animation setting instance and the subclass of the `AnimationBase`) and you can animate x-directional scale with it from a specified x-coordinate.

Similarly, the `animation_scale_y_from_point` method interface will create an `ap.AnimationScaleYFromPoint` instance and you can animate y-directional scale with it from a specified y-coordinate.

These interfaces exist on a `GraphicsBase` subclass (that has the `scale_x_from_center` and `scale_y_from_center` interfaces), such as the `Rectangle` or `Circle`.

## Basic usage

The following example sets the x-directional scale (left-side rectangle) and y-directional scale (right-side rectangle) animation (from 1.0 to 2.0) with the `animation_scale_x_from_point` and `animation_scale_y_from_point` methods.

The left-side rectangle will scale from the left end (x=50) and the right-side rectangle will scale from the bottom end (y=100).

```py
# runnable
from enum import Enum

from typing_extensions import TypedDict

import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT
LEFT_RECTANGLE_X: int = 50
RIGHT_RECTANGLE_Y: int = 100
SCALE_1: float = 1.0
SCALE_2: float = 2.0


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
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_point(
            scale_x_from_point=SCALE_1,
            x=LEFT_RECTANGLE_X,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_point(
            scale_y_from_point=SCALE_1,
            y=RIGHT_RECTANGLE_Y,
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
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_point(
            scale_x_from_point=SCALE_2,
            x=LEFT_RECTANGLE_X,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_point(
            scale_y_from_point=SCALE_2,
            y=RIGHT_RECTANGLE_Y,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()


stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

options: Options = {'direction': Direction.X}
left_rectangle.animation_scale_x_from_point(
    scale_x_from_point=SCALE_2,
    x=LEFT_RECTANGLE_X,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

options = {'direction': Direction.Y}
right_rectangle.animation_scale_y_from_point(
    scale_y_from_point=SCALE_2,
    y=RIGHT_RECTANGLE_Y,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

ap.save_overall_html(
    dest_dir_path='./animation_scale_x_and_y_from_point_basic_usage/')
```

<iframe src="static/animation_scale_x_and_y_from_point_basic_usage/index.html" width="250" height="150"></iframe>

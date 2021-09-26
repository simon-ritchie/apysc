# animation_reset interface

This page will explain the `animation_reset` method interface.

## What interface is this?

The `animation_reset` interface will reset all animations and stop.

This interface exists in the instances that have the animation interfaces (such as the `animation_x`, `animation_move`).

## Basic usage

The following example will set the click event to the rectangle and if you click the rectangle x-coordinate animation will start. After 1 second passed the x-coordinate animation will reset by the `animation_reset` interface:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.Rectangle
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.animation_x(x=500, duration=3000).start()
    options_: _RectOptions = {'rectangle': e.this}
    timer: ap.Timer = ap.Timer(
        on_timer, delay=1000, repeat_count=1, options=options_)
    timer.start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options['rectangle'].animation_reset()


stage: ap.Stage = ap.Stage(
    stage_width=600, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='./animation_reset_basic_usage/')
```

<iframe src="static/animation_reset_basic_usage/index.html" width="600" height=150></iframe>

# animation_finish interface

This page will explain the `animation_finish` method interface.

## What interface is this?

The `animation_finish` interface will finish all running animations and set the last attribute values of each animation setting.

This interface exists in the instances that have the animation interfaces (such as the `animation_x`, `animation_move`).

## Basic usage

The following example will set the click event to the rectangle and if you click the rectangle x-coordinate animation will start. After 2 seconds passed the x-coordinate animation will finish and set the last x-coordinate value of the animation.

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
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.animation_x(
        x=300, duration=5000,
    ).start()

    options_: _RectOptions = {'rectangle': rectangle}
    ap.Timer(
        on_timer, delay=2000, repeat_count=1, options=options_,
    ).start()


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.animation_finish()


ap.Stage(
    stage_width=400, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='animation_finish_basic_usage/')
```

<iframe src="static/animation_finish_basic_usage/index.html" width="400" height="150"></iframe>

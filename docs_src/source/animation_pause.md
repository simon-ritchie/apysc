# animation_pause interface

This page will explain the `animation_pause` method interface.

## What interface is this?

The `animation_pause` interface will pause all the running animations of the target instance.

This interface exists in the instances that have the animation interfaces (such as the `animation_x`, `animation_move`).

## Basic usage

The following example will start x-coordinate animation and stop after 1 second. After stopping the animation and additionally 500 milliseconds passed, restarting the animation:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options['rectangle'].animation_pause()
    timer: ap.Timer = ap.Timer(
        on_timer_2, delay=500, options=options, repeat_count=1)
    timer.start()


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    options['rectangle'].animation_play()


stage: ap.Stage = ap.Stage(
    stage_width=600, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_x(x=500, duration=15_000).start()

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    on_timer_1, delay=1000, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='./animation_pause_basic_usage/')
```

<iframe src="static/animation_pause_basic_usage/index.html" width="600" height="150"></iframe>

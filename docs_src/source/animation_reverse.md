# animation_reverse interface

This page explains the `animation_reverse` method interface.

## What interface is this?

The `animation_reverse` interface reverses the running animations.

This interface exists in the instances that have the animation interfaces (such as the `animation_x`\, `animation_move`).

## Basic usage

The following example sets the x-coordinate animation and starts the 1-second interval timer to reverse animation with the `animation_reverse` interface.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The event handler that timer calls after the 3 seconds.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.Timer(on_timer_2, delay=1000, options=options).start()


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The event handler that timer calls every second.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.animation_reverse()


ap.Stage(
    stage_width=500, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_x(x=400, duration=5000).start()
options: _RectOptions = {'rectangle': rectangle}
ap.Timer(
    on_timer_1, delay=3000, repeat_count=1,
    options=options).start()

ap.save_overall_html(
    dest_dir_path='animation_reverse_basic_usage/')
```

<iframe src="static/animation_reverse_basic_usage/index.html" width="500" height="150"></iframe>

## Interface Notes

This interface can only use during animation. If you use this at the end of the animation, nothing happens, as follows:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']

    # Nothing happens since the animation has already been completed.
    rectangle.animation_reverse()


ap.Stage(
    stage_width=500, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_x(x=400, duration=1000).start()

options: _RectOptions = {'rectangle': rectangle}
ap.Timer(on_timer, delay=1500, repeat_count=1, options=options).start()

ap.save_overall_html(
    dest_dir_path='animation_reverse_notes/')
```

<iframe src="static/animation_reverse_notes/index.html" width="500" height="150"></iframe>
# TimerEvent class

This page will explain the `TimerEvent` class.

## What class is this?

The `TimerEvent` class is the event class that would be passed to a timer event handler function.

The handler would be passed to the `Timer` class constructor handler and the `timer_complete` interfaces event instance will be this event instance.

## Basic usage

Each timer event handler's `e` argument will be `TimerEvent` class instance.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1


def on_timer_complete(e: ap.TimerEvent, options: dict) -> None:
    """
    The handler would be called when the timer is complete.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Timer complete!')


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=33.3, options=options)
timer.start()
timer.timer_complete(handler=on_timer_complete)

ap.save_overall_html(
    dest_dir_path='timer_event_basic_usage/')
```

<iframe src="static/timer_event_basic_usage/index.html" width="150" height="150"></iframe>

## This attribute

The `TimerEvent` instance's `this` attribute will be the target `Timer` instance, and you can use each timer instance interface from it.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_timer(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler would be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.rotation_around_center += 1
    ap.trace('Current timer count: ', e.this.current_count)


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

options: _RectOptions = {'rectangle': rectangle}
timer: ap.Timer = ap.Timer(
    handler=on_timer, delay=16.6, options=options)
timer.start()

ap.save_overall_html(
    dest_dir_path='timer_event_this_attribute/')
```

<iframe src="static/timer_event_this_attribute/index.html" width="150" height="150"></iframe>

# Bind and trigger the custom event

This page will explain the `bind_custom_event` and `trigger_custom_event` interfaces.

## What interfaces are these?

The `bind_custom_event` interface will register your original event to the instance, and the `trigger_custom_event` one will trigger registered custom events at any timing.

## Basic usage

The `bind_custom_event` interface has the `custom_event_type`, `handler`, `e`, and `options` arguments (`options` is optional).

The `custom_event_type` argument is the custom event type name string. This value needs to specify the same string at the calling of the `trigger_custom_event` interface.

The `e` argument is an event instance, which may be become the subclass of the `Event` class, such as the `MouseEvent` or `TimerEvent` and so on.

The following example will rotate the rectangle when you click it. If the rectangle is rotated 90 degrees, then the custom event (`rotate_90_degrees`) will be triggered and the `on_rotate_90_degrees` handler (custom event) will be called and display the second rectangle (toggle the `visible` property):

```py
# runnable
from typing import Any
from typing import Dict

import apysc as ap

# Custom event type name.
ROTATE_90_DEGREES: str = 'rotate_90_degrees'


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[str, Any]):
    """
    The handler would be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.unbind_click(on_rectangle_click)
    timer: ap.Timer = ap.Timer(
        on_timer, delay=ap.FPS.FPS_60, repeat_count=90,
        options={'rectangle': e.this})
    timer.timer_complete(
        on_timer_complete,
        options={'rectangle': e.this})
    timer.start()


def on_timer(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
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


def on_timer_complete(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called when a time is complete.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.trigger_custom_event(custom_event_type=ROTATE_90_DEGREES)


def on_rotate_90_degrees(e: ap.Event, options: Dict[str, Any]) -> None:
    """
    The handler would be called when the rectangle is rotated
    90 degrees (custom event).

    Parameters
    ----------
    e : ap.Event
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.visible = ap.Boolean(True)


stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_1.click(on_rectangle_click)
rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.visible = ap.Boolean(False)

e: ap.Event = ap.Event(this=rectangle_1)
rectangle_1.bind_custom_event(
    custom_event_type=ROTATE_90_DEGREES, handler=on_rotate_90_degrees, e=e,
    options={'rectangle': rectangle_2})

ap.save_overall_html(
    dest_dir_path='bind_and_trigger_custom_event_basic_usage/')
```

<iframe src="static/bind_and_trigger_custom_event_basic_usage/index.html" width="250" height="150"></iframe>

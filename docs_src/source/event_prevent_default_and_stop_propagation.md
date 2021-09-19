# Event class prevent_default and stop_propagation interfaces

This page will explain the `Event` class `prevent_default` and `stop_propagation` method interfaces.

## What interfaces are these?

The `prevent_default` method interface will append the calling expression of the JavaScript `preventDefault` method. This will prevent the browser default behavior of any event.

The `stop_propagation` method interface will stop an event propagation, for example, the triggered child event will not propagate to a parent event (parent event will not be triggered).

## Basic usage of the prevent_default interface

The `Event` instance and its subclass instance have the `prevent_default` method. The `prevent_default` method requires no arguments, as follows:

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.prevent_default()


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='event_prevent_default_basic_usage/')
```

## Basic usage of the stop_propagation interface

The `Event` instance and its subclass instance have the `stop_propagation` method. The `stop_propagation` method, like the `prevent_default` one, requires no arguments.

The following example will bind the click event to the sprite and rectangle instances. The rectangle (child) click handler will call the `stop_propagation` method so the sprite (parent) click handler will not be called:

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.stop_propagation()
    ap.trace('The rectangle is clicked!')


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: Dict[Any, Any]) -> None:
    """
    The handler will be called when the sprite is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('The sprite is clicked!')


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.click(on_sprite_click)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='event_stop_propagation_basic_usage/')
```

If you click the following rectangle, the only message of `The rectangle is clicked!` will be displayed browser console (please press the F12 key), and the sprite console message will not be displayed.

<iframe src="static/event_stop_propagation_basic_usage/index.html" width="150" height="150"></iframe>

## Notes for the TimerEvent class

The `TimerEvent` class (subclass of the `Event`) is disabled the `prevent_default` and `stop_propagation` interfaces and if you call these interfaces, the error will be raised:

```py
from typing import Any, Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[Any, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.prevent_default()


timer: ap.Timer = ap.Timer(on_timer, delay=1000)
```

```
NotImplementedError: `TimerEvent` class is not supported the `prevent_default`interface.
```

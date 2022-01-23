# Event class prevent_default and stop_propagation interfaces

This page explains the `Event` class `prevent_default` and `stop_propagation` method interfaces.

## What interfaces are these?

The `prevent_default` method interface appends the calling expression of the JavaScript `preventDefault` method. This interface prevents the browser default behavior of any event.

The `stop_propagation` method interface stops an event's propagation; for example, the triggered child event does not propagate to a parent event (it ignores the parent event).

## Basic usage of the prevent_default interface

The `Event` instance and its subclass instance have the `prevent_default` method. The `prevent_default` method requires no arguments, as follows:

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.prevent_default()


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='event_prevent_default_basic_usage/')
```

## Basic usage of the stop_propagation interface

The `Event` instance and its subclass instance have the `stop_propagation` method. The `stop_propagation` method, like the `prevent_default` one, requires no arguments.

The following example binds the click event to the sprite and rectangle instances. The rectangle (child) click handler calls the `stop_propagation` method, so the sprite (parent) doesn't call the click handler:

```py
# runnable
import apysc as ap


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

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
        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('The sprite is clicked!')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.click(on_sprite_click)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='event_stop_propagation_basic_usage/')
```

If you click the following rectangle, the only message of `The rectangle is clicked!` is displayed browser console (please press the F12 key). Also, the sprite console message is not displayed.

<iframe src="static/event_stop_propagation_basic_usage/index.html" width="150" height="150"></iframe>
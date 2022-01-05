# Mousedown and mouseup interfaces

This page explains the `mousedown` and `mouseup` interfaces.

## What interfaces are these?

The `mousedown` interface binds the event handler that the interface calls when a user mouse downed on a `DisplayObject` instance. Conversely, the `mouseup` interface binds the event handler that the interface calls when a user mouse upped on a `DisplayObject` one.

## See also

The following page describes the basic mouse event interfaces:

- [Basic mouse event interfaces](mouse_event_basic.md)

## Basic usage of the mousedown and mouseup interfaces

Each `DisplayObject` instance has the `mousedown` and `mouseup` method interfaces, and you can bind handlers by these.

The following example binds the mouse down handler and mouse upped one to the rectangle. The handler changes the rectangle color when the mouse downs and reverts to the original one when the mouse upped.

```py
# runnable
import apysc as ap


def on_mousedown(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousedown.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


def on_mouseup(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseup.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#0af')


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Bind each handler to the rectangle.
rectangle.mousedown(on_mousedown)
rectangle.mouseup(on_mouseup)

ap.save_overall_html(
    dest_dir_path='mousedown_and_mouseup_basic_usage/')
```

<iframe src="static/mousedown_and_mouseup_basic_usage/index.html" width="150" height="150"></iframe>

## Unbind interfaces

The `unbind_mousedown` and `unbind_mouseup` interfaces unbind each registered handler from the `DisplayObject`\.

The following example unbinds handlers in the `on_mousedown` and `on_mouseup` functions so that the rectangle calls these handlers only once.

```py
# runnable
import apysc as ap


def on_mousedown(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousedown.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.unbind_mousedown(handler=on_mousedown)
    rectangle.fill_color = ap.String('#f0a')


def on_mouseup(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseup.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.unbind_mouseup(handler=on_mouseup)
    rectangle.fill_color = ap.String('#0af')


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle.mousedown(on_mousedown)
rectangle.mouseup(on_mouseup)

ap.save_overall_html(
    dest_dir_path='mousedown_and_mouseup_unbind_interfaces/')
```

<iframe src="static/mousedown_and_mouseup_unbind_interfaces/index.html" width="150" height="150"></iframe>

There are also existing the `unbind_mousedown_all` and `unbind_mouseup_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.

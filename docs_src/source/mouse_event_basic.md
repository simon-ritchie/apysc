# Basic mouse event interfaces

This page explains the basic mouse event interfaces, like the `this` attribute.

## Basic binding usage

Each mouse event binding interface accepts `handler` and `options` arguments. The `handler` argument is each interface's callable object when event dispatching.

The `options` argument is an optional parameter dictionary to be passed to the handler. You can skip this argument.

For instance, you can set the `click` event as follows:

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


class _ColorOptions(TypedDict):
    color: str


def on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: ap.Rectangle = e.this
    color: ap.String = ap.String(options['color'])
    rectangle.fill_color = color


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _ColorOptions = {'color': '#f0a'}
rectangle.click(
    handler=on_rectangle_click, options=options)

ap.save_overall_html(
    dest_dir_path='mouse_event_basic_basic_binding_usage/')
```

If you click the rectangle, the handler changes the rectangle color to the specified options color.

<iframe src="static/mouse_event_basic_basic_binding_usage/index.html" width="150" height="150"></iframe>

There are many mouse events binding interfaces, such as the `click`\, `mousedown`\, `mouseup`\, `mouseover`\, `mouseout`\, and `mousemove` that the `DisplayObject` instance has.

## Basic unbinding usage

Each `DisplayObject` instance has the `unbind_<event_name>` interfaces, for example, `unbind_click` or `unbind_mousedown` or something else.

These interfaces can unbind the single handler setting (remove binding setting).

For example, the following code unbinds the click event, so the interface doesn't call the handler function.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


class _ColorOptions(TypedDict):
    color: str


def on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: ap.Rectangle = e.this
    color: ap.String = ap.String(options['color'])
    rectangle.fill_color = color


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _ColorOptions = {'color': '#f0a'}
rectangle.click(
    handler=on_rectangle_click, options=options)

rectangle.unbind_click(handler=on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='mouse_event_basic_basic_unbinding_usage/')
```

When you click the following rectangle, nothing happens.

<iframe src="static/mouse_event_basic_basic_unbinding_usage/index.html" width="150" height="150"></iframe>

## Unbind all event handlers

Sometimes, it is helpful to unbind specific all the events at once. For example, each event interface has the `unbind_<event_name>_all` method (e.g., `unbind_click_all`). It can unbind all event handlers from that instance.

The following code calls the `unbind_click_all` method and removes all handler settings.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


class _ColorOptions(TypedDict):
    color: str


def change_color_on_rectangle_click(
        e: ap.MouseEvent, options: _ColorOptions) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    color: ap.String = ap.String(options['color'])
    rectangle.fill_color = color


def change_x_on_rectangle_click(
        e: ap.MouseEvent, options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.x += 50


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _ColorOptions = {'color': '#f0a'}
rectangle.click(
    handler=change_color_on_rectangle_click, options=options)
rectangle.click(handler=change_x_on_rectangle_click)

rectangle.unbind_click_all()

ap.save_overall_html(
    dest_dir_path='mouse_event_basic_unbind_all_event_handlers/')
```

Nothing happens when clicking the rectangle (no color change and no x-coordinate change).

<iframe src="static/mouse_event_basic_unbind_all_event_handlers/index.html" width="150" height="150"></iframe>

## Handler argument names and types

Handler function (or method) first argument requires the type of the `MouseEvent`\.

Also, a second argument name is required to be `options`\. This argument type becomes `dict`\. If you skip options argument specification at binding the event, then this argument becomes a blank dictionary (`{}`).

## MouseEvent this attribute

The `MouseEvent` instance has the `this` attribute, which becomes an event target instance. So, if you bind the click event to the rectangle instance, the `this` attribute becomes that rectangle instance.

## MouseEvent generic type settings

Suppose you know that you only use one of the handlers by an instance of a particular type. In that case, you can set generic type settings to the `MouseEvent` type annotation (e.g., `MouseEvent[Rectangle]`).

This setting is helpful to determine the `this` attribute type, and the type-checking library, such as the `mypy` or `Pylance`\, checks the instance type.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_rectangle_mousedown(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousedown.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle = e.this
    rectangle.x += 50


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.mousedown(handler=on_rectangle_mousedown)
```

## MouseEvent stage_x and stage_y attributes

MouseEvent instance has the `stage_x` and `stage_y` attributes. These attributes are absolute coordinates from the upper-left position of the stage.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_mousemove(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    ap.trace('stage_x:', e.stage_x, 'stage_y:', e.stage_y)


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=100, width=50, height=50)
rectangle.mousemove(handler=on_mousemove)

ap.save_overall_html(
    dest_dir_path='mouse_event_basic_stage_x_and_stage_y')
```

If you open the DevTools console on Chrome (press F12) and move the mouse cursor on the following rectangle, you can check the `stage_x` and `stage_y` coordinates. The previous code positions the rectangle at `(50, 100)`, so the `stage_x` becomes the range of 50 to 100, and `stage_y` becomes 100 to 150.

<iframe src="static/mouse_event_basic_stage_x_and_stage_y/index.html" width="150" height="200"></iframe>

## MouseEvent local_x and local_y attributes

MouseEvent instance also has `local_x` and `local_y` attributes. These attributes are the local coordinates from the event registered instance position.

The following example shows that local_x and local_y become the coordinates in the rectangle area. Both of the `local_x` and `local_y` become a range of 0 to 50 because the rectangle size is 50-pixel.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_mousemove(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    ap.trace('local_x:', e.local_x, 'local_y:', e.local_y)


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.mousemove(handler=on_mousemove)

ap.save_overall_html(
    dest_dir_path='mouse_event_basic_local_x_and_local_y')
```

Please check on Chrome DevTools (press F12) and move the mouse cursor on the following rectangle.

<iframe src="static/mouse_event_basic_local_x_and_local_y/index.html" width="150" height="150"></iframe>

## See also

- [Click interface](click.md)
- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [Mousemove interface](mousemove.md)
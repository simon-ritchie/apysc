# Common mouse event interfaces

This page will explain the common mouse event interfaces, like `this`.

## Basic binding usage

Each mouse event binding interface accepts `handler` and `options` arguments. The `handler` argument is a callable called when the target event is dispatched.

The `options` argument is an optional parameter dictionary to be passed to the handler. This argument can be skipped.

For instance, the `click` event can be set as follows:

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent
from apysc import String
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def on_rectangle_click(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: Rectangle = e.this
    color: String = String(options['color'])
    rectangle.fill_color = color


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(
    handler=on_rectangle_click,
    options={'color': '#f0a'})

save_expressions_overall_html(
    dest_dir_path='mouse_event_common_basic_binding_usage/')
```

If you click the following rectangle, the rectangle color will be changed to the specified options color.

<iframe src="static/mouse_event_common_basic_binding_usage/index.html" width="150" height="150"></iframe>

There are the `click`, `mousedown`, `mouseup`, `mouseover`, `mouseout`, and `mousemove` mouse event binding interfaces that the `DisplayObject` instance has.

## Basic unbinding usage

Each `DisplayObject` instance has the `unbind_<event_name>` interfaces, for example, `unbind_click` or `unbind_mousedown` or something else.

These interfaces can unbind the single handler setting (remove binding setting).

For example, the following code will unbind the click event, so the handler function will not be called.

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent
from apysc import String
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def on_rectangle_click(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: Rectangle = e.this
    color: String = String(options['color'])
    rectangle.fill_color = color


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(
    handler=on_rectangle_click,
    options={'color': '#f0a'})

rectangle.unbind_click(handler=on_rectangle_click)

save_expressions_overall_html(
    dest_dir_path='mouse_event_common_basic_unbinding_usage/')
```

When you click the following rectangle, nothing will happen.

<iframe src="static/mouse_event_common_basic_unbinding_usage/index.html" width="150" height="150"></iframe>

## Unbind all event handlers

Sometimes, it is useful to unbind specific all the event at once. Each event interface has the `unbind_<event_name>_all` method (e.g., `unbind_click_all`), and it can unbind all event handlers from that instance.

The following code is calling the `unbind_click_all` method, so all hander settings are removed.

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent
from apysc import String
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def change_color_on_rectangle_click(
        e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    The handler will change the rectangle color and be called
    when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: Rectangle = e.this
    color: String = String(options['color'])
    rectangle.fill_color = color


def change_x_on_rectangle_click(
        e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    The handler will change the rectangle x-coordinate and be called
    when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: Rectangle = e.this
    rectangle.x += 50


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(
    handler=change_color_on_rectangle_click,
    options={'color': '#f0a'})
rectangle.click(handler=change_x_on_rectangle_click)

rectangle.unbind_click_all()

save_expressions_overall_html(
    dest_dir_path='mouse_event_common_unbind_all_event_handlers/')
```

If you click the following rectangle, also nothing will happen (no color change and no x-coordinate change).

<iframe src="static/mouse_event_common_unbind_all_event_handlers/index.html" width="150" height="150"></iframe>

## Handler argument names and types

Handler function (or method) first argument name is required to be `e`, not `evt` or `event`. And that argument type will be `MouseEvent`.

Also, a second argument name is required to be `options`. This argument type will be `dict`. If you skipped options argument specification at binding the event, then this argument will become a blank dictionary (`{}`).

## MouseEvent this attribute

`MouseEvent` instance has the `this` attribute, and this will be an instance that the event handler is set. For example, if you bind the click event to the rectangle instance, the `this` attribute will be that rectangle instance.

## MouseEvent generic type settings

If you know that one of the handlers will only be used by an instance of a particular type, you can set generic type settings to the `MouseEvent` type annotation (e.g., `MouseEvent[Rectangle]`).

This is useful to determine the `this` attribute type and will be checked by the `mypy`, `Pylance`, or other type checkers.

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def on_rectangle_mousedown(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler will be called when the rectangle is mouse downed.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle = e.this
    rectangle.x += 50


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.mousedown(handler=on_rectangle_mousedown)
```

## MouseEvent stage_x and stage_y attributes

MouseEvent instance has the `stage_x` and `stage_y` attributes. These attributes are absolute coordinates from the upper-left position of the stage.

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent
from apysc import trace
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def on_mousemove(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler will be called when the mouse is moving on
    the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    trace('stage_x:', e.stage_x, 'stage_y:', e.stage_y)


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=100, width=50, height=50)
rectangle.mousemove(handler=on_mousemove)

save_expressions_overall_html(
    dest_dir_path='mouse_event_common_stage_x_and_stage_y')
```

If you open the DevTools console on Chrome (press F12) and move the mouse cursor on the following rectangle, you can check the `stage_x` and `stage_y` coordinates. The rectangle is positioned at `(50, 100)`, so the `stage_x` will become the range of 50 to 100, and `stage_y` will become 100 to 150.

<iframe src="static/mouse_event_common_stage_x_and_stage_y/index.html" width="150" height="200"></iframe>

## MouseEvent local_x and local_y attributes

MouseEvent instance also has `local_x` and `local_y` attributes. These attributes are the local coordinates from the event registered instance position.

The following example will show that local_x and local_y will become the coordinates in the rectangle area (both `local_x` and `local_y` will be the range of 0 to 50, because the rectangle size is 50-pixel).

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent
from apysc import trace
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def on_mousemove(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler will be called when the mouse is moving on
    the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    trace('local_x:', e.local_x, 'local_y:', e.local_y)


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.mousemove(handler=on_mousemove)

save_expressions_overall_html(
    dest_dir_path='mouse_event_common_local_x_and_local_y')
```

Please check on Chrome DevTools (press F12) and move the mouse cursor on the following rectangle.

<iframe src="static/mouse_event_common_local_x_and_local_y/index.html" width="150" height="150"></iframe>

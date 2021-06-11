# Mousedown and mouseup interfaces

This page will explain the `mousedown` and `mouseup` interfaces.

## What interfaces are these?

The `mousedown` interface will bind the event handler called when a user mouse downed on a `DisplayObject` instance. Conversely, the `mouseup` interface will bind the event handler called when a user mouse upped on a `DisplayObject` one.

## See also

Common mouse event interfaces are described by the following page.

- [Common mouse event interfaces](mouse_event_common.md)

## Basic usage of the mousedown and mouseup interfaces

Each `DisplayObject` instance has the `mousedown` and `mouseup` method interfaces, and you can bind handlers by these.

The following example will bind the mouse down handler and mouse upped one to the rectangle. The rectangle color will change the different color when you did mouse downed and will revert to the original one when you did mouse upped.

```py
# runnable
from typing import Any, Dict

from apysc import Rectangle
from apysc import MouseEvent
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc import save_expressions_overall_html


def on_mousedown(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a mouse is downed on the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: Rectangle = e.this
    rectangle.fill_color = String('#f0a')


def on_mouseup(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a mouse is upped on the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: Rectangle = e.this
    rectangle.fill_color = String('#0af')


stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Bind each handler to the rectangle.
rectangle.mousedown(on_mousedown)
rectangle.mouseup(on_mouseup)

save_expressions_overall_html(
    dest_dir_path='mousedown_and_mouseup_basic_usage/')
```

<iframe src="static/mousedown_and_mouseup_basic_usage/index.html" width="150" height="150"></iframe>

## Unbind interfaces

The `unbind_mousedown` and `unbind_mouseup` interfaces will unbind each registered handler from `DisplayObject`.

The following example will unbind handlers in the `on_mousedown` and `on_mouseup` function so these handlers will be called only once.

```py
# runnable
from typing import Any, Dict

from apysc import Rectangle
from apysc import MouseEvent
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc import save_expressions_overall_html


def on_mousedown(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a mouse is downed on the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: Rectangle = e.this
    rectangle.unbind_mousedown(handler=on_mousedown)
    rectangle.fill_color = String('#f0a')


def on_mouseup(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a mouse is upped on the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: Rectangle = e.this
    rectangle.unbind_mouseup(handler=on_mouseup)
    rectangle.fill_color = String('#0af')


stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle.mousedown(on_mousedown)
rectangle.mouseup(on_mouseup)

save_expressions_overall_html(
    dest_dir_path='mousedown_and_mouseup_unbind_interfaces/')
```

<iframe src="static/mousedown_and_mouseup_unbind_interfaces/index.html" width="150" height="150"></iframe>

There are also existing the `unbind_mousedown_all` and `unbind_mouseup_all` interfaces. These interfaces will unbind all the handlers from the target `DisplayObject` instance.

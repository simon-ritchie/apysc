# Mousemove interface

This page will explain the `mousemove` interface.

## What interface is this?

`mousemove` interface will bind the mouse moving event handler to any `DisplayObject` instance. If you move the mouse cursor on that instance the registered handler will be called.

## See also

Common mouse event interfaces are described by the following page.

- [Common mouse event interfaces](mouse_event_common.md)

## Basic usage

Each `DisplayObject` instance has the `mousemove` method, and you can bind handlers by that.

The following example will bind the mouse move event handler to the circle and if you move a mouse cursor on that, the circle will follow the cursor position.

```py
# runnable
from typing import Any
from typing import Dict

from apysc import MouseEvent
from apysc import Sprite
from apysc import Stage
from apysc import Circle
from apysc import save_overall_html


def on_mousemove(e: MouseEvent[Circle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a mouse cursor is moved
    on the circle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
circle: Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)

save_overall_html(
    dest_dir_path='mousemove_basic_usage/')
```

<iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

## Unbind interfaces

`unbind_mousemove` interface can remove the binding of the mouse move event from the `DisplayObject`.

In the following example, if you click the circle then the mouse move event handler will be removed.

```py
# runnable
from typing import Any
from typing import Dict

from apysc import MouseEvent
from apysc import Sprite
from apysc import Stage
from apysc import Circle
from apysc import save_overall_html


def on_mousemove(e: MouseEvent[Circle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a mouse cursor is moved
    on the circle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


def on_click(e: MouseEvent[Circle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the circle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: Circle = e.this
    circle.unbind_mousemove(handler=on_mousemove)


stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
circle: Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)
circle.click(on_click)

save_overall_html(
    dest_dir_path='mousemove_unbind_interface/')
```

<iframe src="static/mousemove_unbind_interface/index.html" width="200" height="200"></iframe>

There are also existing the `unbind_mousemove_all` interface. This interface will unbind all the handlers from the target `DisplayObject` instance.

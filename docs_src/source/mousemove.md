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
import apysc as ap


def on_mousemove(
        e: ap.MouseEvent[ap.Circle], options: dict) -> None:
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
    circle: ap.Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)

ap.save_overall_html(
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

import apysc as ap


def on_mousemove(
        e: ap.MouseEvent[ap.Circle], options: dict) -> None:
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
    circle: ap.Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


def on_click(e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler would be called when the circle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.unbind_mousemove(handler=on_mousemove)


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)
circle.click(on_click)

ap.save_overall_html(
    dest_dir_path='mousemove_unbind_interface/')
```

<iframe src="static/mousemove_unbind_interface/index.html" width="200" height="200"></iframe>

There are also existing the `unbind_mousemove_all` interface. This interface will unbind all the handlers from the target `DisplayObject` instance.

# Click and unbind_click interface

This page will explain the `click` and `unbind_click` interfaces.

## What interfaces are these?

`click` interface will bind the click event to any `DisplayObject` instance (e.g., `Sprite`, `Rectangle`, and so on). If you mouse down on that instance and also mouse up, the registered handler function will be called.

Conversely, the `unbind_click` interface will unbind the click event from the `DisplayObject` instance.

## See also

Common mouse event interfaces are described by the following page.

- [Common mouse event interfaces](mouse_event_common.md)

## Basic usage of the click interface

Each `DisplayObject` instance has the `click` method, and you can bind handlers by that.

The following example will bind the click event to the rectangle.

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


def on_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.
    the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: Rectangle = e.this
    rectangle.fill_color = String('#f0a')


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)

save_expressions_overall_html(
    dest_dir_path='click_basic_usage_of_the_click_interface')
```

If you click the following rectangle, the rectangle color will become the magenta color.

<iframe src="static/click_basic_usage_of_the_click_interface/index.html" width="150" height="150"></iframe>


## Basic usage of the unbind_click interface

`unbind_click` interface can remove the binding click event from the `DisplayObject` instance.

Following example is removing the click event by the `unbind_click` method (if you click the rectangle, nothing will happen).

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


def on_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.
    the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: Rectangle = e.this
    rectangle.fill_color = String('#f0a')


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=100, width=50, height=50)
rectangle.click(handler=on_click)
rectangle.unbind_click(handler=on_click)

save_expressions_overall_html(
    dest_dir_path='click_basic_usage_of_the_unbind_click_interface')
```

<iframe src="static/click_basic_usage_of_the_unbind_click_interface/index.html" width="150" height="150"></iframe>

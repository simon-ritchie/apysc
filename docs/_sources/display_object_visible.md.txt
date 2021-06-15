# Display object visible interface

This page will explain the `DisplayObject` class `visible` property interface.

## What interface is this?

The `visible` property interface will change the `DisplayObject` visible / invisible state.

## Basic usage

The `visible` property accepts a `Boolean` value. If you set the True value then a `DisplayObject` instance will be visible (default), conversely if you set the False value then a `DisplayObject` instance will be invisible.

The following example will switch the visible values when you click the rectangle. If you click the left rectangle (rectangle_1) then the left rectangle will be invisible and right rectangle (rectangle_2) will be visible.

```py
# runnable
from typing import Any, Dict

from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import MouseEvent
from apysc import Boolean
from apysc import save_overall_html


def on_rectangle_1_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the first rectangle
    is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: Rectangle = e.this
    rectangle_2: Rectangle = options['rectangle_2']
    rectangle_1.visible = Boolean(False)
    rectangle_2.visible = Boolean(True)


def on_rectangle_2_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the second rectangle
    is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: Rectangle = options['rectangle_1']
    rectangle_2: Rectangle = e.this
    rectangle_1.visible = Boolean(True)
    rectangle_2.visible = Boolean(False)


stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)

sprite.graphics.begin_fill(color='#0af')
rectangle_1: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

sprite.graphics.begin_fill(color='#f0a')
rectangle_2: Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.visible = Boolean(False)

rectangle_1.click(
    on_rectangle_1_click, options={'rectangle_2': rectangle_2})
rectangle_2.click(
    on_rectangle_2_click, options={'rectangle_1': rectangle_1})

save_overall_html(dest_dir_path='display_object_visible_basic_usage/')
```

<iframe src="static/display_object_visible_basic_usage/index.html" width="250" height="150"></iframe>

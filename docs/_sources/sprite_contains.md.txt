# Sprite class contains interface

This page will explain the `Sprite` class (or the other container class, like the `Graphics`) `contains` method interface.

## What interface is this?

The `contains` interface will return the boolean (`Boolean`) value whether that `Sprite` instance has a given child or not.

## Basic usage

The following example will check whether the first rectangle is a child of the `Sprite` container and if it is true then remove the rectangle from the sprite and display a log to the console (please press F12 to display that message).

```py
# runnable
from typing import Any
from typing import Dict

from apysc import MouseEvent
from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import Boolean
from apysc import If
from apysc import save_overall_html, trace


def on_sprite_click(
        e: MouseEvent[Sprite], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the sprite instance is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: Sprite = e.this
    rectangle_1: Rectangle = options['rectangle_1']
    condition: Boolean = sprite.graphics.contains(child=rectangle_1)
    with If(condition):
        sprite.remove_child(child=rectangle_1)
        trace('Removed the rectangle!')


stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle_1: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
sprite.click(
    on_sprite_click,
    options={'rectangle_1': rectangle_1})

save_overall_html(dest_dir_path='sprite_contains_basic_usage/')
```

<iframe src="static/sprite_contains_basic_usage/index.html" width="250" height="150"></iframe>

## See also

- [Sprite class add child and remove child interfaces](sprite_add_child_and_remove_child.md)

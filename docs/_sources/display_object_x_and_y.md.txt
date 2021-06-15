# Display object x and y interfaces

This page will explain the `DisplayObject` class `x` and `y` property interfaces.

## What interfaces are these?

The `x` and `y` properties will change the `DisplayObject` instance 2-dimensional coordinates.

## Basic usage

Each `DisplayObject` instance has the `x` and `y` properties and can get or set the value with it.

```py
# runnable
from apysc import Stage
from apysc import Sprite
from apysc import Rectangle
from apysc import Int
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=0, y=0, width=50, height=50)

# Update the x and y coordinates from 0 to 50.
rectangle.x = Int(50)
rectangle.y = Int(50)

save_overall_html(dest_dir_path='display_object_x_and_y_basic_usage/')
```

<iframe src="static/display_object_x_and_y_basic_usage/index.html" width="150" height="150"></iframe>

## Augmented assignment

The `x` and `y` properties support the Augmented assignments, like the `+=`, `-=`, `/=`, and `*=` operators.

The following example will append 10-pixel to the y-coordinate when you click the rectangle.

```py
# runnable
from typing import Any, Dict

from apysc import Stage
from apysc import Sprite
from apysc import Rectangle
from apysc import MouseEvent
from apysc import save_overall_html


def on_click(e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: Rectangle = e.this
    rectangle.y += 10


stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

save_overall_html(
    dest_dir_path='display_object_x_and_y_augmented_assignment/')
```

<iframe src="static/display_object_x_and_y_augmented_assignment/index.html" width="150" height="150"></iframe>

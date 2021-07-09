# Graphics move_to and line_to interfaces

This page will explain the `Graphics` class `move_to` and `line_to` method interfaces.

## What interfaces are they?

`move_to` interface will set the line start point. and `line_to` will draw the line from a current point to a destination point. If you call the `line_to` interface sequentially, then the line will be polyline.

Calling the `move_to` interface after the calling of `line_to`, then a new line instance will be created.

## Basic usage

`move_to` and `line_to` interfaces are both having x and y arguments.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=300,
    stage_height=100,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.line_style(color='#0af', thickness=5)

# Move to x=50, y=50 point (no drawing).
sprite.graphics.move_to(x=50, y=50)

# Draw the line from the current point (50, 50) to the
# destination point (250, 50).
sprite.graphics.line_to(x=250, y=50)

ap.save_overall_html(
    dest_dir_path='graphics_move_to_and_line_to_basic_usage/')
```

<iframe src="static/graphics_move_to_and_line_to_basic_usage/index.html" width="300" height="100"></iframe>

## Sequential calling of the line_to interface.

If you call the `line_to` interface sequentially, then the result line will become the polyline.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.line_style(color='#0af', thickness=5)

# Move to x=50, y=50 point (no drawing).
sprite.graphics.move_to(x=50, y=50)

# Draw the line from the current point (50, 50) to the
# destination point (150, 50).
sprite.graphics.line_to(x=150, y=50)

# Draw the line from the current point (250, 50) to the
# destination point (50, 150). This will change the line
# to the polyline.
sprite.graphics.line_to(x=50, y=150)

# Finally the polyline becomes Z shape by drawing to
# destination point (150, 150).
sprite.graphics.line_to(x=150, y=150)

ap.save_overall_html(
    dest_dir_path='graphics_move_to_and_line_to_sequential_calling/')
```

<iframe src="static/graphics_move_to_and_line_to_sequential_calling/index.html" width="200" height="200"></iframe>

## move_to interface calling after line_to interface calling

If you call the `move_to` interface after calling the `line_to` interface, then a new line instance will be created.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.line_style(color='#0af', thickness=5)

# First move_to interface calling.
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=100, y=50)
sprite.graphics.line_to(x=50, y=100)
sprite.graphics.line_to(x=100, y=100)

# Second move_to interface calling. This will create a new
# polyline instance.
sprite.graphics.move_to(x=150, y=50)
sprite.graphics.line_to(x=200, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

ap.save_overall_html(
    dest_dir_path='graphics_move_to_and_line_to_multi_move_to_calling/')
```

<iframe src="static/graphics_move_to_and_line_to_multi_move_to_calling/index.html" width="250" height="150"></iframe>

## Polyline instance

`move_to` and `line_to` interfaces will return `Polyline` instance. You can update each setting or bind events to that instance.

For instance, the following script will set the mouse event to `Polyline` and updating the line color, and set dot style in the handler (`on_line_click`).

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_line_click(
        e: ap.MouseEvent[ap.Polyline], options: Dict[str, Any]) -> None:
    """
    The handler that this will be called when the line instance
    is clicked.

    Parameters
    ----------
    e : MouseEvent
        The event instance.
    options : dict
        Optional arguments.
    """
    polyline: ap.Polyline = e.this
    polyline.line_color = ap.String('#f0a')
    polyline.line_dot_setting = ap.LineDotSetting(dot_size=5)


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.line_style(color='#0af', thickness=30)
polyline: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=150, y=50)
polyline.click(on_line_click)

ap.save_overall_html(
    dest_dir_path='graphics_move_to_and_line_to_polyline/')
```

If you click the following line, line style will be updated:

<iframe src="static/graphics_move_to_and_line_to_polyline/index.html" width="200" height="100"></iframe>

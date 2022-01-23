# Graphics move_to and line_to interfaces

This page explains the `Graphics` class `move_to` and `line_to` method interfaces.

## What interfaces are they?

The `move_to` interface sets the line start point. The `line_to` draws the line from a current point to a destination point. Sequentially, if you call the `line_to` interface, the line becomes polyline.

If you call the `move_to` interface after the calling of `line_to`\, it creates a new line instance.

## Basic usage

The `move_to` and `line_to` interfaces have x and y arguments.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=300,
    stage_height=100,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

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

## Sequential calling of the line_to interface

Sequentially, if you call the `line_to` interface, the result line becomes the polyline.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color='#0af', thickness=5)

# Move to x=50, y=50 point (no drawing).
sprite.graphics.move_to(x=50, y=50)

# Draw the line from the current point (50, 50) to the
# destination point (150, 50).
sprite.graphics.line_to(x=150, y=50)

# Draw the line from the current point (250, 50) to the
# destination point (50, 150). This calling changes the line
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

If you call the `move_to` interface after calling the `line_to` interface, it creates a new line instance.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

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

For instance, the following script sets the mouse event to `Polyline`\, updates the line color, and sets dot style in the handler (`on_line_click`).

```py
# runnable
import apysc as ap


def on_line_click(
        e: ap.MouseEvent[ap.Polyline], options: dict) -> None:
    """
    The handler that the line instance calls when clicked.

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


ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color='#0af', thickness=30)
polyline: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=150, y=50)
polyline.click(on_line_click)

ap.save_overall_html(
    dest_dir_path='graphics_move_to_and_line_to_polyline/')
```

If you click the following line, line style will be updated:

<iframe src="static/graphics_move_to_and_line_to_polyline/index.html" width="200" height="100"></iframe>
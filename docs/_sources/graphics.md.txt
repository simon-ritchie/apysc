# Graphics

This page will explain the `Graphics` class.

## What is Graphics?

The `Graphics` is the class to handle each vector graphics interface. This interface has the draw rectangle interface, draw line interface, or something else.

This class instance is instantiated by the `Sprite` or other `DisplayObject` instances.

## Call interfaces from sprite instance

Sprite (object container) instance has the `graphics` attribute so with this attribute, each drawing interface can be called.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=180,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite(stage=stage)

# Draw the white border and cyan color rectangle.
sprite.graphics.line_style(color='#fff', thickness=5)
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Draw the magenta color polyline.
sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(color='#f0a', thickness=5)
sprite.graphics.move_to(x=150, y=50)
sprite.graphics.line_to(x=200, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

# Draw the dashed line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=130, x_end=200, y_end=130,
    dash_size=10, space_size=5)

ap.save_overall_html(
    dest_dir_path='graphics_call_interfaces_from_sprite_instance/')
```

<iframe src="static/graphics_call_interfaces_from_sprite_instance/index.html" width="250" height="180"></iframe>

## Return values

Each interface will return created graphic instances (e.g., `Rectangle`, `Polyline`, and so on). These instances have the basic `DisplayObject` attributes and methods, like x, y, fill_alpha, visible, or something else.

For example, you can set an event and coordinates updating to these instances, as follows:

```py
# runnable
from typing import Any, Dict

import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite(stage=stage)


def on_rectangle_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[str, Any]) -> None:
    """
    A Handler that called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this

    # Update the coordinates, fill alpha, and fill color.
    rectangle.x = ap.Int(100)
    rectangle.y = ap.Int(100)
    rectangle.fill_alpha = ap.Number(0.5)
    rectangle.fill_color = ap.String('#f0a')


# drew_rect interface will return Rectangle instance.
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Bind click event to the rectangle.
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='graphics_return_values/')
```

If you click the following rectangle, that rectangle will change x and y coordinates, fill color, and alpha (opacity) values.

<iframe src="static/graphics_return_values/index.html" width="200" height="200"></iframe>

## See also

- [Graphics class begin fill interface](graphics_begin_fill.md)
- [Graphics class line style interface](graphics_line_style.md)
- [Graphics class draw rect interface](graphics_draw_rect.md)
- [Graphics class draw round rect interface](graphics_draw_round_rect.md)
- [Graphics class draw circle interface](graphics_draw_circle.md)
- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)
- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)
- [Graphics class draw line interface](graphics_draw_line.md)
- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)
- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)
- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)
- [Graphics class draw polygon interface](graphics_draw_polygon.md)

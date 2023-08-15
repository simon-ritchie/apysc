# Graphics class

This page explains the `Graphics` class.

## What is Graphics?

The `Graphics` is the class to handle each vector graphics interface. This interface has the draw rectangle interface, draw line interface, or something else.

The `Sprite` or other `DisplayObject` instances instantiate this class instance.

## Call interfaces from sprite instance

Sprite (object container) instance has the `graphics` attribute to call each drawing interface with this attribute.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=180,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()

# Draw the white border and cyan color rectangle.
sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Draw the magenta color polyline.
sprite.graphics.begin_fill(color=ap.COLORLESS)
sprite.graphics.line_style(color=ap.Color("#f0a"), thickness=5)
sprite.graphics.move_to(x=150, y=50)
sprite.graphics.line_to(x=200, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

# Draw the dashed line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=130, x_end=200, y_end=130, dash_size=10, space_size=5
)

ap.save_overall_html(dest_dir_path="graphics_call_interfaces_from_sprite_instance/")
```

<iframe src="static/graphics_call_interfaces_from_sprite_instance/index.html" width="250" height="180"></iframe>

## Return values

Each interface returns created graphic instances (e.g., `Rectangle`\, `Polyline`\, and so on). These instances have the basic `DisplayObject` attributes and methods, like x, y, fill_alpha, visible, or something else.

For example, you can set an event and coordinate's updating to these instances, as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=200,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this

    # Update the coordinates, fill alpha, and fill color.
    rectangle.x = ap.Number(100)
    rectangle.y = ap.Number(100)
    rectangle.fill_alpha = ap.Number(0.5)
    rectangle.fill_color = ap.Color("#f0a")


# drew_rect interface will return Rectangle instance.
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Bind click event to the rectangle.
rectangle.click(on_rectangle_click)

ap.save_overall_html(dest_dir_path="graphics_return_values/")
```

If you click the following rectangle, that rectangle changes x and y coordinates, fill color, and alpha (opacity) values.

<iframe src="static/graphics_return_values/index.html" width="200" height="200"></iframe>

## See also

- [Graphics class begin_fill interface](graphics_begin_fill.md)
- [Graphics class line_style interface](graphics_line_style.md)
- [Graphics class draw_rect interface](graphics_draw_rect.md)
- [Graphics class draw_round_rect interface](graphics_draw_round_rect.md)
- [Graphics class draw_circle interface](graphics_draw_circle.md)
- [Graphics class draw_ellipse interface](graphics_draw_ellipse.md)
- [Graphics class move_to and line_to interfaces](graphics_move_to_and_line_to.md)
- [Graphics class draw_line interface](graphics_draw_line.md)
- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)
- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)
- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)
- [Graphics class draw_polygon interface](graphics_draw_polygon.md)
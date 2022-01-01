# Graphics line_color interface

This page explains the `Graphics` class `line_color` property interface.

## What interface is this?

The `line_color` property interface updates or get the instance's line color.

## Basic usage

The getter or setter interface becomes (or requires) the `String` hex color code value.

The following example changes the line color (from cyan to magenta and magenta to cyan) when you click the rectangle:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
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
    line_color: ap.String = rectangle.line_color
    with ap.If(line_color == '#00aaff'):
        rectangle.line_color = ap.String('#f0a')
    with ap.Else():
        rectangle.line_color = ap.String('#0af')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0', alpha=0.0)
sprite.graphics.line_style(color='#0af', thickness=5)

rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='./graphics_line_color_basic_usage/')
```

<iframe src="static/graphics_line_color_basic_usage/index.html" width="150" height="150"></iframe>

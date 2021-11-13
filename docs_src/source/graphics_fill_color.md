# Graphics fill_color interface

This page will explain the `Graphics` class `fill_color` method interface.

## What interface is this?

The `fill_color` attribute interface will update the instance's fill color.

## Basic usage

The getter interface will be the `String` hex color code value and the setter one also requires the `String` hex color code value.

The following example will change the fill color (from cyan to magenta, and magenta to cyan) when you click the rectangle:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    fill_color: ap.String = rectangle.fill_color
    with ap.If(fill_color == '#00aaff'):
        rectangle.fill_color = ap.String('#f0a')
    with ap.Else():
        rectangle.fill_color = ap.String('#0af')


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='./graphics_fill_color_basic_usage/')
```

<iframe src="static/graphics_fill_color_basic_usage/index.html" width="150" height="150"></iframe>

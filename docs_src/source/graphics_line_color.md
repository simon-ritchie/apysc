# Graphics line_color interface

This page explains the `Graphics` class `line_color` property interface.

## What interface is this?

The `line_color` property interface updates or get the instance's line color.

## Basic usage

The getter or setter interface value becomes (or requires) the `String` hex color code value.

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


## line_color property API

<!-- Docstring: apysc._display.line_color_interface.LineColorInterface.line_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get this instance's line color.<hr>

**[Returns]**

- `line_color`: String
  - Current line color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_color = ap.String('#0af')
>>> line.line_color
String('#00aaff')
```
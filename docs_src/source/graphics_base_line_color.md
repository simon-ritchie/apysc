# GraphicsBase line_color interface

This page explains the `GraphicsBase` class `line_color` property interface.

## What interface is this?

The `line_color` property interface updates or get the instance's line color.

## Basic usage

The getter or setter interface value becomes (or requires) a `Color` value.

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
    line_color: ap.Color = rectangle.line_color
    with ap.If(line_color == ap.Color("#00aaff")):
        rectangle.line_color = ap.Color("#f0a")
    with ap.Else():
        rectangle.line_color = ap.Color("#0af")


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0"), alpha=0.0)
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="./graphics_base_line_color_basic_usage/")
```

<iframe src="static/graphics_base_line_color_basic_usage/index.html" width="150" height="150"></iframe>


## line_color property API

<!-- Docstring: apysc._display.line_color_mixin.LineColorMixIn.line_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get this instance's line color.<hr>

**[Returns]**

- `line_color`: Color
  - Current line color (hexadecimal string, e.g., '#00aaff'). If it is not set, it returns the `COLORLESS` constant.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=150,
...     stage_height=150,
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=50,
...     y=50,
...     width=50,
...     height=50,
...     line_color=ap.Color("#0af"),
...     line_thickness=2,
... )
>>> rectangle.line_color
Color("#00aaff")

>>> rectangle.line_color = ap.Color("#ff00aa")
>>> rectangle.line_color
Color("#ff00aa")
```
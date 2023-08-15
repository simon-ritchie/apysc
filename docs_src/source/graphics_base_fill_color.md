# GraphicsBase fill_color interface

This page explains the `GraphicsBase` class `fill_color` property interface.

## What interface is this?

The `fill_color` property interface updates or get the instance's fill color.

## Basic usage

The getter interface becomes a `Color` value, and the setter one also requires a `Color` value.

The following example changes the fill color (from cyan to magenta and magenta to cyan) when you click the rectangle:

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
    fill_color: ap.String = rectangle.fill_color
    with ap.If(fill_color == "#00aaff"):
        rectangle.fill_color = ap.Color("#f0a")
    with ap.Else():
        rectangle.fill_color = ap.Color("#0af")


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="./graphics_base_fill_color_basic_usage/")
```

<iframe src="static/graphics_base_fill_color_basic_usage/index.html" width="150" height="150"></iframe>


## fill_color property API

<!-- Docstring: apysc._display.fill_color_mixin.FillColorMixIn.fill_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get this instance's fill color.<hr>

**[Returns]**

- `fill_color`: String
  - Current fill color (hexadecimal string color, e.g., '#00aaff'). If it is not set, it returns the `COLORLESS` constant.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.fill_color = ap.Color("#f0a")
>>> rectangle.fill_color
Color("#ff00aa")
```
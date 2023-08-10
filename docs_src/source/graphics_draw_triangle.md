
# Graphics draw_triangle interface

This page explains the `Graphics` class `draw_triangle` method interface.

## What interface is this?

The `draw_triangle` interface draws vector triangle graphics.

## Basic usage

The `draw_triangle` interface requires the `x1`, `y1`, `x2`, `y2`, `x3`, and `y3` arguments.

The `x1` and `y1` arguments are the first vertex coordinate of a triangle.

The `x2` and `y2` are the second vertex coordinate, and the `x3` and `y3` are the third.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
triangle: ap.Triangle = sprite.graphics.draw_triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
)

ap.save_overall_html(dest_dir_path="./graphics_draw_triangle_basic_usage/")
```

<iframe src="static/graphics_draw_triangle_basic_usage/index.html" width="150" height="150"></iframe>

## Triangle instance

The `draw_triangle` interface returns a `Triangle` instance.

You can update each setting or bind events.

For instance, the following example sets the mouse event to the `Triangle` instance and updates the x-coordinate in the `on_click` handler:

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Rectangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle: ap.Triangle = e.this
    triangle.x += 2


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
triangle: ap.Triangle = sprite.graphics.draw_triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
)
triangle.click(handler=on_click)

ap.save_overall_html(dest_dir_path="./graphics_draw_triangle_triangle_instance/")
```

<iframe src="static/graphics_draw_triangle_triangle_instance/index.html" width="150" height="150"></iframe>

## draw_triangle API

<!-- Docstring: apysc._display.graphics.Graphics.draw_triangle -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_triangle(self, *, x1: Union[float, apysc._type.number.Number], y1: Union[float, apysc._type.number.Number], x2: Union[float, apysc._type.number.Number], y2: Union[float, apysc._type.number.Number], x3: Union[float, apysc._type.number.Number], y3: Union[float, apysc._type.number.Number], variable_name_suffix: str = '') -> apysc._display.triangle.Triangle`<hr>

**[Interface summary]**

Draw a triangle vector graphic.<hr>

**[Parameters]**

- `x1`: Union[float, Number]
  - First vertex's x coordinate.
- `y1`: Union[float, Number]
  - First vertex's y coordinate.
- `x2`: Union[float, Number]
  - Second vertex's x coordinate.
- `y2`: Union[float, Number]
  - Second vertex's y coordinate.
- `x3`: Union[float, Number]
  - Third vertex's x coordinate.
- `y3`: Union[float, Number]
  - Third vertex's y coordinate.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `triangle`: Triangle
  - Created triangle graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.7)
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=0.5)
>>> triangle: ap.Triangle = sprite.graphics.draw_triangle(
...     x1=75,
...     y1=50,
...     x2=25,
...     y2=100,
...     x3=100,
...     y3=100,
... )
>>> triangle.x1
Number(75.0)

>>> triangle.y1 = ap.Number(30)
>>> triangle.y1
Number(30.0)

>>> triangle.fill_color
String("#00aaff")
```

<hr>

**[References]**

- [Triangle class](https://simon-ritchie.github.io/apysc/en/triangle.html)
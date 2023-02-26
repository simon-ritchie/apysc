# Graphics draw_rect interface

This page explains the `Graphics` class `draw_rect` method interface.

## What interface is this?

`draw_rect` interface draws vector rectangle graphics.

## Basic usage

`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates settings, and `width` and `height` determine rectangle size.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")
sprite.graphics.draw_rect(x=50, y=50, width=100, height=50)

ap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage/")
```

The previous script draws horizontal rectangle graphics.

<iframe src="static/graphics_draw_rect_basic_usage/index.html" width="200" height="150"></iframe>

Notes: `begin_fill` call (fill color setting) is necessary before a `draw_rect` interface call. If you skip it, it displays nothing on stage.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.draw_rect(x=50, y=50, width=100, height=50)

ap.save_overall_html(dest_dir_path="graphics_draw_rect_basic_usage_skipped_begin_fill/")
```

<iframe src="static/graphics_draw_rect_basic_usage_skipped_begin_fill/index.html" width="200" height="150"></iframe>

## Rectangle instance

`draw_rect` interface will return a `Rectangle` instance. You can update each setting or bind events.

For instance, the following script sets the mouse event to `Rectangle` and updates the x position in the handler (`on_click`).

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.x = ap.Int(100)


ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color="#0af")
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="graphics_draw_rect_rectangle/")
```

If you click rectangle, the handler changes the x position to 100.

<iframe src="static/graphics_draw_rect_rectangle/index.html" width="200" height="150"></iframe>


## draw_rect API

<!-- Docstring: apysc._display.graphics.Graphics.draw_rect -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_rect(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], width: Union[int, apysc._type.int.Int], height: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> apysc._display.rectangle.Rectangle`<hr>

**[Interface summary]**

Draw a rectangle vector graphics.<hr>

**[Parameters]**

- `x`: float or Number
  - X position to start drawing.
- `y`: float or Number
  - Y position to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `rectangle`: Rectangle
  - Created rectangle.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.x
Number(50.0)

>>> rectangle.width
Int(50)

>>> rectangle.fill_color
String("#00aaff")
```
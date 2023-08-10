# Graphics draw_dashed_line interface

This page explains the `Graphics` class `draw_dashed_line` method interface.

## What interface is this?

`draw_dashed_line` interface will draw the simple straight dashed-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.

## Basic usage

`draw_dashed_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dash_size` and `space_size` arguments to determine dash style (line dash size and the space size between each dash).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=130,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 5-pixel dash setting and draw the line.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=2)
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=50, x_end=200, y_end=50, dash_size=5, space_size=2
)

# Set 10-pixel dash setting and draw the line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=80, x_end=200, y_end=80, dash_size=10, space_size=2
)

ap.save_overall_html(dest_dir_path="graphics_draw_dashed_line_basic_usage/")
```

<iframe src="static/graphics_draw_dashed_line_basic_usage/index.html" width="250" height=130></iframe>


## draw_dashed_line API

<!-- Docstring: apysc._display.graphics.Graphics.draw_dashed_line -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_dashed_line(self, *, x_start: Union[float, apysc._type.number.Number], y_start: Union[float, apysc._type.number.Number], x_end: Union[float, apysc._type.number.Number], y_end: Union[float, apysc._type.number.Number], dash_size: Union[int, apysc._type.int.Int], space_size: Union[int, apysc._type.int.Int], variable_name_suffix: str = '') -> '_line.Line'`<hr>

**[Interface summary]**

Draw a dashed line vector graphics.<hr>

**[Parameters]**

- `x_start`: float or Number
  - Line start x-coordinate.
- `y_start`: float or Number
  - Line start y-coordinate.
- `x_end`: float or Number
  - Line end x-coordinate.
- `y_end`: float or Number
  - Line end y-coordinate.
- `dash_size`: Int or int
  - Dash size.
- `space_size`: Int or int
  - Blank space size between dashes.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDotSetting`, except `LineDashSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dashed_line(
...     x_start=50, y_start=50, x_end=150, y_end=50, dash_size=5, space_size=2
... )
>>> line.line_color
String("#ffffff")

>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```
# Graphics draw_line interface

This page explains the `Graphics` class `draw_line` method interface.

## What interface is this?

`draw_line` interface will draw the simple straight line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.

## Basic usage

`draw_line` inteface has `x_start` (line x-start coordinate), `y_start` (line y-start coordinate), `x_end` (line x-end coordinate), and `y_end` (line y-end coordinate) arguments.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_draw_line_basic_usage/")
```

<iframe src="static/graphics_draw_line_basic_usage/index.html" width="200" height=100></iframe>

## Ignored line style settings

This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting` for simplicity. If you need to draw these styled lines, then use `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, or `draw_dash_dotted_line` interfaces instead of the `draw_line` interface.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# dot_setting will be ignored, and the result line will not be dotted.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    dot_setting=ap.LineDotSetting(dot_size=5),
)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_draw_line_ignored_dot_setting/")
```

<iframe src="static/graphics_draw_line_ignored_dot_setting/index.html" width="200" height=100></iframe>

## Line class instance

`draw_line` interface returns the `Line` instance. You can update each setting or bind events to that instance. `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`
, and `draw_dash_dotted_line` will also return the same type instance.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=100,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.line_style(color=ap.Color("#0af"), thickness=5)
line: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

# Update the line color from cyan to magenta.
line.line_color = ap.Color("#f0a")

ap.save_overall_html(dest_dir_path="graphics_draw_line_line_instance/")
```

<iframe src="static/graphics_draw_line_line_instance/index.html" width="200" height=100></iframe>


## draw_line API

<!-- Docstring: apysc._display.graphics.Graphics.draw_line -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_line(self, *, x_start: Union[float, apysc._type.number.Number], y_start: Union[float, apysc._type.number.Number], x_end: Union[float, apysc._type.number.Number], y_end: Union[float, apysc._type.number.Number], variable_name_suffix: str = '') -> '_line.Line'`<hr>

**[Interface summary]**

Draw a normal line vector graphic.<hr>

**[Parameters]**

- `x_start`: float or Number
  - Line start x-coordinate.
- `y_start`: float or Number
  - Line start y-coordinate.
- `x_end`: float or Number
  - Line end x-coordinate.
- `y_end`: float or Number
  - Line end y-coordinate.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDotSetting`, `LineDashSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_color
Color("#ffffff")

>>> line.line_thickness
Int(5)
```
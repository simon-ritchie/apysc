# Graphics line_style interface

This page explains the `Graphics` class `line_style` method interface.

## What interface is this?

The `line_style` interface sets each line style, such as the line color, line alpha, line thickness, line dot setting. This interface maintains these settings until it is called again or called the `clear` method (similar to the `begin_fill` interface).

## Basic usage

Draw vector graphics interfaces (e.g., the `draw_rect` or `line_to`) use these line settings when creating. Therefore, calling the `line_style` method is necessary before calling each drawing interface.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=162,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Draw a white line with 3px line thickness.
sprite.graphics.line_style(color=ap.Color("#ccc"), thickness=8)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=150, y=50)

# Line style setting will be maintained.
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=150, y=80)

# Change line color and thickness.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=3)
sprite.graphics.move_to(x=50, y=110)
sprite.graphics.line_to(x=150, y=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_basics/")
```

<iframe src="static/graphics_line_style_basics/index.html" width="200" height="162"></iframe>

## Line-color setting

The required `color` argument sets the line color.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=102,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set a cyan line color and draw the line.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_color/")
```

<iframe src="static/graphics_line_style_line_color/index.html" width="200" height="102"></iframe>

If you want to clear line color, specify a blank string to this argument.

For example, the result line graphic becomes invisible since the following code clears the line color setting.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=102,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set a cyan line color.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=4)

# Clear the line color by specifying the `COLORLESS` constant.
sprite.graphics.line_style(color=ap.COLORLESS, thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

ap.save_overall_html(dest_dir_path="graphics_line_style_clear_line_color/")
```

<iframe src="static/graphics_line_style_clear_line_color/index.html" width="200" height="102"></iframe>

Color code is acceptable like the following list (same as `begin_fill` interface `color` argument):

- Six characters, e.g., `#00aaff`.
- Three characters, e.g., `#0af` (this becomes `#00aaff`).
- Single character, e.g., `#5` (this becomes `#000005`).
- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).
- The `COLORLESS` constant (this clears line color setting).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200, stage_height=162, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

# The six characters line color setting (a cyan color).
sprite.graphics.line_style(color=ap.Color("#00aaff"), thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# The three characters line color setting (a magenta color).
sprite.graphics.line_style(color=ap.Color("#f0a"), thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)

# The one character line color setting (a black color).
sprite.graphics.line_style(color=ap.Color("#5"), thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_color_color_code/")
```

<iframe src="static/graphics_line_style_line_color_color_code/index.html" width="200" height="162"></iframe>

## Line thickness setting

The `thickness` argument sets the line thickness. It can accept greater than or equal to 1.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=165,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 1-pixel line thickness.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=1)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# Set 4-pixel line thickness.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)

# Set 10-pixel line thickness.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=10)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_thickness/")
```

<iframe src="static/graphics_line_style_thickness/index.html" width="200" height="165"></iframe>

## Line alpha (opacity) setting

A line alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Draw the cyan line from upper-left to lower-right.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=15, alpha=0.3)
sprite.graphics.draw_line(x_start=50, x_end=100, y_start=50, y_end=100)

# Draw the magenta line from upper-right to lower-left.
sprite.graphics.line_style(color=ap.Color("#f0a"), thickness=15, alpha=0.3)
sprite.graphics.draw_line(x_start=100, x_end=50, y_start=50, y_end=100)

ap.save_overall_html(dest_dir_path="graphics_line_style_alpha/")
```

<iframe src="static/graphics_line_style_alpha/index.html" width="150" height="150"></iframe>

## Line cap setting

Line cap setting changes line edge style. The `cap` argument sets this style setting, and `LineCaps` enum values are acceptable.

There are three `LineCaps` options, as follows:

- BUTT: This is the default value, and it sets no cap.
- ROUND: This changes the line edge to the rounded one.
- SQUARE: This is similar to BUTT, but it increases the line length by the squared edge.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=180,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# BUTT caps setting (default).
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=20, cap=ap.LineCaps.BUTT)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# ROUND caps setting.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=20, cap=ap.LineCaps.ROUND)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=90, y_end=90)

# SQUARE caps setting (same line length setting as BUTT line,
# but this will be longer for the caps).
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=20, cap=ap.LineCaps.SQUARE)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=130, y_end=130)

ap.save_overall_html(dest_dir_path="graphics_line_style_caps/")
```

<iframe src="static/graphics_line_style_caps/index.html" width="200" height="180"></iframe>

## Line joints setting

Line joints setting changes the line vertices style. The `joints` argument sets this style, and `LineJoints` enum values are acceptable. The `Polyline` class (`move_to` and `line_to` interfaces) mainly uses this argument.

There are three LineJoints enum values, as follows:

- MITER: This setting sets the style like a picture frame vertices. This setting is the default style setting.
- ROUND: This setting sets the rounded vertices style.
- BEVEL: This setting sets a beveled vertices style.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=350,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set MITER joints setting and draw the polyline.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=10, joints=ap.LineJoints.MITER)
sprite.graphics.move_to(x=50, y=100)
sprite.graphics.line_to(x=75, y=50)
sprite.graphics.line_to(x=100, y=100)

# Set ROUND joints setting and draw the polyline.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=10, joints=ap.LineJoints.ROUND)
sprite.graphics.move_to(x=150, y=100)
sprite.graphics.line_to(x=175, y=50)
sprite.graphics.line_to(x=200, y=100)

# Set BEVEL joints setting and draw the polyline.
sprite.graphics.line_style(color=ap.Color("#0af"), thickness=10, joints=ap.LineJoints.BEVEL)
sprite.graphics.move_to(x=250, y=100)
sprite.graphics.line_to(x=275, y=50)
sprite.graphics.line_to(x=300, y=100)

ap.save_overall_html(dest_dir_path="graphics_line_style_joints/")
```

<iframe src="static/graphics_line_style_joints/index.html" width="350" height="150"></iframe>

## Line dot setting

Line dot setting changes the line to dotted line. The `dot_setting` argument (`LineDotSetting` value) sets this setting. It can change dot size by the `dot_size` argument (greater than or equal to 1 value is acceptable).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=160,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set the line dot settings with 2-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    dot_setting=ap.LineDotSetting(dot_size=2),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set the line dot settings with 5-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    dot_setting=ap.LineDotSetting(dot_size=5),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

# Set the line dot settings with 10-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    dot_setting=ap.LineDotSetting(dot_size=10),
)
sprite.graphics.move_to(x=50, y=110)
sprite.graphics.line_to(x=250, y=110)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting/")
```

<iframe src="static/graphics_line_style_line_dot_setting/index.html" width="300" height="160"></iframe>

This setting (or the other similar settings) also changes the `Rectangle` or other graphics classes.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set the line dot setting with 2-pixel dot size and draw the rectangle.
# Fill color setting is skipped.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    dot_setting=ap.LineDotSetting(dot_size=2),
)
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Draw the rectangle with the dotted line setting and the fill color.
sprite.graphics.begin_fill(color=ap.Color("#038"))
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dot_setting_rectangle/")
```

<iframe src="static/graphics_line_style_line_dot_setting_rectangle/index.html" width="250" height="150"></iframe>

Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.

## Line dash setting

Line dash setting changes the line to the dashed line. The `dash_setting` argument (`LineDashSetting` value) sets this setting. It can change dash size and space size by the `dash_size` and `space_size` arguments.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=130,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 10-pixel dash size and 3-pixel space size and draw the line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=3,
    dash_setting=ap.LineDashSetting(dash_size=10, space_size=3),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 15-pixel dash size and 5-pixel space size and draw the line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=3,
    dash_setting=ap.LineDashSetting(dash_size=15, space_size=5),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_setting/")
```

<iframe src="static/graphics_line_style_line_dash_setting/index.html" width="300" height="130"></iframe>

Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.

## Line round dot setting

Line round dot setting changes the line to the round dotted line. The `round_dot_setting` argument (`LineRoundDotSetting` value) sets this setting. It can change round size and space size by the `round_size` and `space_size` arguments.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=130,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    round_dot_setting=ap.LineRoundDotSetting(round_size=5, space_size=5),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 10-pixel round size and draw the line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=5,
    round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_round_dot_setting/")
```

<iframe src="static/graphics_line_style_line_round_dot_setting/index.html" width="300" height="130"></iframe>

Notes: Since this setting uses the `cap` setting internally, this setting ignores the `cap` setting, increasing the line length by the capsize.

Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.

## Line dash-dot setting

Line dash-dot setting changes the line to the dash-dotted line (also called long dashed short dashed line or one-dot chain line). The `dash_dot_setting` arguments set this setting and it accepts a `LineDashDotSetting` instance. This argument accepts the `dot_size` (short dashed size), `dash_size` (long dashed size), and `space_size` arguments.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=300,
    stage_height=130,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

# Set 3-pixel dot size and 10-pixel dash size and draw the line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=3,
    dash_dot_setting=ap.LineDashDotSetting(dot_size=3, dash_size=10, space_size=3),
)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 5-pixel dot size and 15-pixel dash size and draw the line.
sprite.graphics.line_style(
    color=ap.Color("#0af"),
    thickness=3,
    dash_dot_setting=ap.LineDashDotSetting(dot_size=5, dash_size=15, space_size=3),
)
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

ap.save_overall_html(dest_dir_path="graphics_line_style_line_dash_dot_setting/")
```

<iframe src="static/graphics_line_style_line_dash_dot_setting/index.html" width="300" height="130"></iframe>

Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.


## line_style API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_style -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `line_style(self, *, color: ~StrOrString, thickness: Union[int, apysc._type.int.Int] = 1, alpha: Union[float, apysc._type.number.Number] = 1.0, cap: Union[apysc._display.line_caps.LineCaps, NoneType] = None, joints: Union[apysc._display.line_joints.LineJoints, NoneType] = None, dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None) -> None`<hr>

**[Interface summary]**

Set line style values.<hr>

**[Parameters]**

- `color`: String or str
  - Hexadecimal color string. e.g., '#00aaff'
- `thickness`: Int or int, default 1
  - Line thickness (minimum value is 1).
- `alpha`: float or Number, default 1.0
  - Line color opacity (0.0 to 1.0).
- `cap`: LineCaps or None, default None
  - Line cap (edge style) setting. The not line-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.
- `joints`: LineJoints or None, default None
  - Line vertices (joints) style setting. The not polyline-related graphics (e.g., Rectangle ignores this, conversely used by Polyline) ignore this setting.
- `dot_setting`: LineDotSetting or None, default None
  - Dot setting. If this is specified, it makes a line dotted.
- `dash_setting`: LineDashSetting or None, default None
  - Dash setting. If this is specified, it makes a line dashed.
- `round_dot_setting`: LineRoundDotSetting or None, default None
  - Round dot setting. If this is specified, it makes a line round dotted. Notes: since this style uses a cap setting, it overrides cap and line thickness settings. And it increases the amount of line size. If you want to adjust to the same width of a normal line when using move_to and line_to interfaces, add half-round size to start x-coordinate and subtract from end e-coordinate. e.g., `this.move_to(x + round_size / 2, y)`, `this.line_to(x - round_size / 2, y)`
- `dash_dot_setting`: LineDashDotSetting or None, default None
  - Dash-dot (1-dot chain) setting. If this is specified, it makes a line 1-dot chained.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"), thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_color
String("#ffffff")

>>> line.line_thickness
Int(5)

>>> line.line_alpha
Number(0.5)

>>> line.line_cap
String("round")
```

## line_color property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line color.<hr>

**[Returns]**

- `line_color`: String
  - Current line color (hexadecimal string, e.g., '#00aaff'). If it is not set, it returns the `COLORLESS` constant.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"), thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> sprite.graphics.line_color
String("#ffffff")
```

## line_thickness property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_thickness -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line thickness.<hr>

**[Returns]**

- `line_thickness`: Int
  - Current line thickness.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=0.5)
>>> sprite.graphics.line_thickness
Int(5)
```

## line_alpha property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_alpha -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line color opacity.<hr>

**[Returns]**

- `line_alpha`: Number
  - Current line opacity (0.0 to 1.0).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"), thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> sprite.graphics.line_alpha
Number(0.5)
```

## line_cap property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_cap -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line cap (edge) style setting.<hr>

**[Returns]**

- `line_cap`: String
  - Current line cap (edge) style setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"), thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
... )
>>> sprite.graphics.line_cap
String("round")
```

## line_joints property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_joints -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line joints (vertices) style setting.<hr>

**[Returns]**

- `line_joints`: String
  - Current line joints (vertices) style setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"), thickness=5, joints=ap.LineJoints.ROUND
... )
>>> sprite.graphics.line_joints
String("round")
```

## line_dot_setting property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_dot_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line dot setting.<hr>

**[Returns]**

- `line_dot_setting`: LineDotSetting or None
  - Current line dot setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"), thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)
... )
>>> sprite.graphics.line_dot_setting.dot_size
Int(5)
```

## line_dash_setting property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_dash_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current line dash setting.<hr>

**[Returns]**

- `line_dash_setting`: LineDashSetting or None
  - Current line dash setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"),
...     thickness=5,
...     dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
... )
>>> sprite.graphics.line_dash_setting.dash_size
Int(10)

>>> sprite.graphics.line_dash_setting.space_size
Int(5)
```

## line_round_dot_setting property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_round_dot_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line-round dot setting.<hr>

**[Returns]**

- `line_round_dot_setting`: LineRoundDotSetting or None
  - Current line round dot setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"),
...     thickness=5,
...     round_dot_setting=ap.LineRoundDotSetting(round_size=6, space_size=3),
... )
>>> sprite.graphics.line_round_dot_setting.round_size
Int(6)

>>> sprite.graphics.line_round_dot_setting.space_size
Int(3)
```

## line_dash_dot_setting property API

<!-- Docstring: apysc._display.line_style_mixin.LineStyleMixIn.line_dash_dot_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current line dash-dot setting.<hr>

**[Returns]**

- `line_dash_dot_setting`: LineDashDotSetting or None
  - Current line dash-dot setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color=ap.Color("#fff"),
...     thickness=5,
...     dash_dot_setting=ap.LineDashDotSetting(
...         dot_size=2, dash_size=5, space_size=3
...     ),
... )
>>> sprite.graphics.line_dash_dot_setting.dot_size
Int(2)

>>> sprite.graphics.line_dash_dot_setting.dash_size
Int(5)

>>> sprite.graphics.line_dash_dot_setting.space_size
Int(3)
```
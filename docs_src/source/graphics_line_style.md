# Graphics line_style interface

This page will explain the `Graphics` class `line_style` method interface.

## What interface is this?

`line_style` interface will set each line style, like the line color, line alpha, line thickness, line dot setting, and so on. This setting will be maintained until it is called again or called the `clear` method (similar to the `begin_fill` interface).

## Basic usage

Draw vector graphics interfaces (e.g., `draw_rect` `line_to` and so on) will use these line settings when they are creating, so the `line_style` method needs to be called before calling each drawing interface.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=162,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Draw a white line with 3px line thickness.
sprite.graphics.line_style(color='#ccc', thickness=8)
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=150, y=50)

# Line style setting will be maintained.
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=150, y=80)

# Change line color and thickness.
sprite.graphics.line_style(color='#0af', thickness=3)
sprite.graphics.move_to(x=50, y=110)
sprite.graphics.line_to(x=150, y=110)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_basics/')
```

<iframe src="static/graphics_line_style_basics/index.html" width="200" height="162"></iframe>

## Line-color setting

A line color will be set by the `color` argument, and this is required one.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=102,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set a cyan line color and draw the line.
sprite.graphics.line_style(color='#0af', thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_line_color/')
```

<iframe src="static/graphics_line_style_line_color/index.html" width="200" height="102"></iframe>

If you want to clear line color, then specify a blank string to this argument.

For example, since the following code will clear line color setting, so a result line graphic is invisible.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=102,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set a cyan line color.
sprite.graphics.line_style(color='#0af', thickness=4)

# Clear the line color by specifying a blank string.
sprite.graphics.line_style(color='', thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_clear_line_color/')
```

<iframe src="static/graphics_line_style_clear_line_color/index.html" width="200" height="102"></iframe>

Color code is acceptable like the following list (same as `begin_fill` interface `color` argument):

- Six characters, e.g., `#00aaff`.
- Three characters, e.g., `#0af` (this will be interpreted as `#00aaff`).
- Single character, e.g., `#5` (this will be interpreted as `#000005`).
- Skipped `#` symbol, e.g., `0af` (this will be interpreted as `#00aaff`).
- Blank string, e.g., `''` (this will clear line color setting).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=162,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# The six characters line color setting (a cyan color).
sprite.graphics.line_style(color='#00aaff', thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# The three characters line color setting (a magenta color).
sprite.graphics.line_style(color='#f0a', thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)

# The one character line color setting (a black color).
sprite.graphics.line_style(color='#5', thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_line_color_color_code/')
```

<iframe src="static/graphics_line_style_line_color_color_code/index.html" width="200" height="162"></iframe>

## Line thickness setting

Line thickness can be set by the `thickness` argument. It can accept greater than or equal to 1.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=165,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set 1-pixel line thickness.
sprite.graphics.line_style(color='#0af', thickness=1)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# Set 4-pixel line thickness.
sprite.graphics.line_style(color='#0af', thickness=4)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=80, y_end=80)

# Set 10-pixel line thickness.
sprite.graphics.line_style(color='#0af', thickness=10)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=110, y_end=110)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_thickness/')
```

<iframe src="static/graphics_line_style_thickness/index.html" width="200" height="165"></iframe>

## Line alpha (opacity) setting

A line alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Draw the cyan line from upper-left to lower-right.
sprite.graphics.line_style(color='#0af', thickness=15, alpha=0.3)
sprite.graphics.draw_line(x_start=50, x_end=100, y_start=50, y_end=100)

# Draw the magenta line from upper-right to lower-left.
sprite.graphics.line_style(color='#f0a', thickness=15, alpha=0.3)
sprite.graphics.draw_line(x_start=100, x_end=50, y_start=50, y_end=100)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_alpha/')
```

<iframe src="static/graphics_line_style_alpha/index.html" width="150" height="150"></iframe>

## Line cap setting

Line cap setting will change line edge style. This can be set by the `cap` argument and `LineCaps` enum values are acceptable.

There are three `LineCaps` options, as follows:

- BUTT: This is the default value, and no cap will be applied.
- ROUND: This will change the line edge to the rounded one.
- SQUARE: This is similar to BUTT, but the line length will be increased by the squared edge.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineCaps
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=180,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# BUTT caps setting (default).
sprite.graphics.line_style(color='#0af', thickness=20, cap=LineCaps.BUTT)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=50, y_end=50)

# ROUND caps setting.
sprite.graphics.line_style(color='#0af', thickness=20, cap=LineCaps.ROUND)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=90, y_end=90)

# SQUARE caps setting (same line length setting as BUTT line,
# but this will be longer for the caps).
sprite.graphics.line_style(color='#0af', thickness=20, cap=LineCaps.SQUARE)
sprite.graphics.draw_line(x_start=50, x_end=150, y_start=130, y_end=130)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_caps/')
```

<iframe src="static/graphics_line_style_caps/index.html" width="200" height="180"></iframe>

## Line joints setting

Line joints setting will change the line vertices style. This can be set by the `joints` argument and `LineJoints` enum values are acceptable. Mainly this argument will be used by the `Polyline` class (`move_to` and `line_to` interfaces).

There are three LineJoints enum values, as follows:

- MITER: This setting will set the style like a picture frame vertices. This is the default style setting.
- ROUND: This setting will set the rounded vertices style.
- BEVEL: This setting will set a sloping vertices style.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineJoints
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set MITER joints setting and draw the polyline.
sprite.graphics.line_style(
    color='#0af', thickness=10, joints=LineJoints.MITER)
sprite.graphics.move_to(x=50, y=100)
sprite.graphics.line_to(x=75, y=50)
sprite.graphics.line_to(x=100, y=100)

# Set ROUND joints setting and draw the polyline.
sprite.graphics.line_style(
    color='#0af', thickness=10, joints=LineJoints.ROUND)
sprite.graphics.move_to(x=150, y=100)
sprite.graphics.line_to(x=175, y=50)
sprite.graphics.line_to(x=200, y=100)

# Set BEVEL joints setting and draw the polyline.
sprite.graphics.line_style(
    color='#0af', thickness=10, joints=LineJoints.BEVEL)
sprite.graphics.move_to(x=250, y=100)
sprite.graphics.line_to(x=275, y=50)
sprite.graphics.line_to(x=300, y=100)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_joints/')
```

<iframe src="static/graphics_line_style_joints/index.html" width="350" height="150"></iframe>

## Line dot setting

Line dot setting will change line to dotted line. This can be set by the `dot_setting` argument. This argument accepts the `LineDotSetting` and can change dot size by the `dot_size` argument (a value that greater than or equal to 1 is acceptable).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineDotSetting
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=300,
    stage_height=160,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set the line dot settings with 2-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color='#0af', thickness=5, dot_setting=LineDotSetting(dot_size=2))
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set the line dot settings with 5-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color='#0af', thickness=5, dot_setting=LineDotSetting(dot_size=5))
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

# Set the line dot settings with 10-pixel dot size and draw the dotted line.
sprite.graphics.line_style(
    color='#0af', thickness=5, dot_setting=LineDotSetting(dot_size=10))
sprite.graphics.move_to(x=50, y=110)
sprite.graphics.line_to(x=250, y=110)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_line_dot_setting/')
```

<iframe src="static/graphics_line_style_line_dot_setting/index.html" width="300" height="160"></iframe>

This setting (or other similar settings) will also be applied to the `Rectangle` or other graphics classes.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineDotSetting
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set the line dot setting with 2-pixel dot size and draw the rectangle.
# Fill color setting is skipped.
sprite.graphics.line_style(
    color='#0af', thickness=5, dot_setting=LineDotSetting(dot_size=2))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Draw the rectangle with the dotted line setting and the fill color.
sprite.graphics.begin_fill(color='#038')
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_line_dot_setting_rectangle/')
```

<iframe src="static/graphics_line_style_line_dot_setting_rectangle/index.html" width="250" height="150"></iframe>

Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.

## Line dash setting

Line dash setting will change line to dashed line. This can be set by the `dash_setting` argument. This argument accepts the `LineDashSetting` and can change dash size and space size by the `dash_size` and `space_size` arguments.

```py
# runnable
from apysc import LineDashSetting
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=300,
    stage_height=130,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set 10-pixel dash size and 3-pixel space size and draw the line.
sprite.graphics.line_style(
    color='#0af', thickness=3,
    dash_setting=LineDashSetting(dash_size=10, space_size=3))
sprite.graphics.move_to(x=50, y=50)
sprite.graphics.line_to(x=250, y=50)

# Set 15-pixel dash size and 5-pixel space size and draw the line.
sprite.graphics.line_style(
    color='#0af', thickness=3,
    dash_setting=LineDashSetting(dash_size=15, space_size=5))
sprite.graphics.move_to(x=50, y=80)
sprite.graphics.line_to(x=250, y=80)

save_expressions_overall_html(
    dest_dir_path='graphics_line_style_line_dash_setting/')
```

<iframe src="static/graphics_line_style_line_dash_setting/index.html" width="300" height="130"></iframe>

Notes: This setting will be ignored by `draw_line`, `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` interfaces.

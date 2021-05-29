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

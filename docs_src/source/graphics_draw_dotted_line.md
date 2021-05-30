# Graphics draw_dotted_line interface

This page will explain the `Graphics` class `draw_dotted_line` method interface.

## What interface is this?

`draw_dotted_line` interface will draw the simple straight dotted-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.

## Basic usage

`draw_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dot_size` argument and it will set line dot size.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=130,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set 2-pixel dot size and draw line.
sprite.graphics.line_style(
    color='#0af', thickness=2)
sprite.graphics.draw_dotted_line(
    x_start=50, y_start=50, x_end=200, y_end=50, dot_size=2)

# Set 5-pixel dot size and draw line.
sprite.graphics.line_style(
    color='#0af', thickness=2)
sprite.graphics.draw_dotted_line(
    x_start=50, y_start=80, x_end=200, y_end=80, dot_size=5)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_dotted_line_basic_usage/')
```

<iframe src="static/graphics_draw_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>

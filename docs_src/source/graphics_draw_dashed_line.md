# Graphics draw_dashed_line interface

This page will explain the `Graphics` class `draw_dashed_line` method interface.

## What interface is this?

`draw_dashed_line` interface will draw the simple straight dashed-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.

## Basic usage

`draw_dashed_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dash_size` and `space_size` arguments to determine dash style (line dash size and the space size between each dash).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=130,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set 5-pixel dash setting and draw the line.
sprite.graphics.line_style(
    color='#0af', thickness=2)
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=50, x_end=200, y_end=50,
    dash_size=5, space_size=2)

# Set 10-pixel dash setting and draw the line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=80, x_end=200, y_end=80,
    dash_size=10, space_size=2)

save_overall_html(
    dest_dir_path='graphics_draw_dashed_line_basic_usage/')
```

<iframe src="static/graphics_draw_dashed_line_basic_usage/index.html" width="250" height=130></iframe>

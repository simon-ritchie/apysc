# Graphics draw_round_dotted_line interface

This page will explain the `Graphics` class `draw_round_dotted_line` method interface.

## What interface is this?

`draw_round_dotted_line` interface will draw the simple straight round dotted-line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, `dash_dot_setting`, and `cap` settings (this is using round cap setting so cap setting will also be ignored).

## Basic usage

`draw_round_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `round_size` and `space_size` arguments to determine the round style (line round size and the space size between each round).

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

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(color='#0af')
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=50, x_end=200, y_end=50,
    round_size=5, space_size=5)

# Set 10-pixel round size and draw the line.
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=80, x_end=200, y_end=80,
    round_size=10, space_size=5)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_round_dotted_line_basic_usage/')
```

<iframe src="static/graphics_draw_round_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>

## Notes

This interface is using the round cap setting, so the line length will be longer by the amount of caps size.

If you want to align the left line position with other lines, then subtract half-round size from other lines `x_start` argument.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=270,
    stage_height=130,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(color='#0af')
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=50, x_end=220, y_end=50,
    round_size=10, space_size=5)

# Set 45-pixel (50 - half-round size) to x_start argument
# and draw the normal line.
sprite.graphics.draw_line(
    x_start=45, y_start=80, x_end=225, y_end=80)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_round_dotted_line_notes/')
```

<iframe src="static/graphics_draw_round_dotted_line_notes/index.html" width="270" height="130"></iframe>

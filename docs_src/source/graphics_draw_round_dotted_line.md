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
    stage_width=200,
    stage_height=130,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set 5-pixel round size and draw the line.
sprite.graphics.line_style(color='#0af')
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=50, x_end=150, y_end=50,
    round_size=5, space_size=5)

# Set 10-pixel round size and draw the line.
sprite.graphics.line_style(color='#0af')
sprite.graphics.draw_round_dotted_line(
    x_start=50, y_start=80, x_end=150, y_end=80,
    round_size=10, space_size=5)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_round_dotted_line_basic_usage/')
```

## Notes



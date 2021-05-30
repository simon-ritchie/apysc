# Graphics draw_line interface

This page will explain the `Graphics` class `draw_line` method interface.

## What interface is this?

`draw_line` interface will draw the simple straight line graphics. This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.

## Basic usage

`draw_line` inteface has `x_start` (line x-start coordinate), `y_start` (line y-start coordinate), `x_end` (line x-end coordinate), and `y_end` (line y-end coordinate) arguments.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

sprite.graphics.line_style(color='#0af', thickness=5)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_line_basic_usage/')
```

<iframe src="static/graphics_draw_line_basic_usage/index.html" width="200" height=100></iframe>

## Ignored line style settings

This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting` for simplicity. If you need to draw these styled lines, then use `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, or `draw_dash_dotted_line` interfaces instead of the `draw_line` interface.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineDotSetting
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# dot_setting will be ignored, and the result line will not be dotted.
sprite.graphics.line_style(
    color='#0af', thickness=5,
    dot_setting=LineDotSetting(dot_size=5))
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_line_ignored_dot_setting/')
```

<iframe src="static/graphics_draw_line_ignored_dot_setting/index.html" width="200" height=100></iframe>

## Line instance

`draw_line` interface will return the `Line` instance. You can update each setting or bind events to that instance. `draw_dotted_line`, `draw_dashed_line`, `draw_round_dotted_line`, and `draw_dash_dotted_line` will also return the same type instance.

```py
# runnable
from apysc import Sprite
from apysc import String
from apysc import Stage
from apysc import Line
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

sprite.graphics.line_style(
    color='#0af', thickness=5)
line: Line = sprite.graphics.draw_line(
    x_start=50, y_start=50, x_end=150, y_end=50)

# Update the line color from cyan to magenta.
line.line_color = String('#f0a')

save_expressions_overall_html(
    dest_dir_path='graphics_draw_line_line_instance/')
```

<iframe src="static/graphics_draw_line_line_instance/index.html" width="200" height=100></iframe>

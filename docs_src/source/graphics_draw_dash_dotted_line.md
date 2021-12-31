# Graphics draw_dash_dotted_line interface

This page will explain the `Graphics` class `draw_dash_dotted_line` method interface.

## What interface is this?

`draw_dash_dotted_line` interface will draw the simple straight dash dotted-line (also called 1-dot chain line or long dashed short dashed line) graphics.

 This interface will ignore `dot_setting`, `dash_setting`, `round_dot_setting`, and `dash_dot_setting`.

## Basic usage

`draw_dash_dotted_line` interface has basic coordinates arguments of `x_start`, `y_start`, `x_end` and `y_end`. That also has `dot_size` (the short dash size), `dash_size` (the long dash size) and `space_size` (the space size between the each dashes) arguments to determine line style.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=130,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set 2-pixel dot size and 6-pixel dash size and draw the line.
sprite.graphics.line_style(color='#0af', thickness=5)
sprite.graphics.draw_dash_dotted_line(
    x_start=50, y_start=50, x_end=200, y_end=50,
    dot_size=2, dash_size=6, space_size=5)

# Set 5-pixel dot size and 10-pixel dash size and draw the line.
sprite.graphics.draw_dash_dotted_line(
    x_start=50, y_start=80, x_end=200, y_end=80,
    dot_size=5, dash_size=10, space_size=5)

ap.save_overall_html(
    dest_dir_path='graphics_draw_dash_dotted_line_basic_usage/')
```

<iframe src="static/graphics_draw_dash_dotted_line_basic_usage/index.html" width="250" height="130"></iframe>

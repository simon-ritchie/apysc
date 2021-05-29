# Graphics begin_fill interface

This page will explain `Graphics` class `begin_fill` method interface.

## What interface is this?

`begin_fill` interface will set the fill color and fill alpha settings. This setting will be maintained until it is called again or called `clear` method.

## Basic usage

Draw vector graphics interfaces (e.g., `draw_rect`) will use these fill settings when they are creating, so `begin_fill` method needs to be called before calling each drawing interface.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set blue fill color and draw first rectangle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Draw second rectangle (fill color setting will be maintained).
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

# Set other fill color and draw third rectangle.
sprite.graphics.begin_fill(color='#f0a')
sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)

save_expressions_overall_html(
    dest_dir_path='graphics_begin_fill_basic_usage/')
```

<iframe src="static/graphics_begin_fill_basic_usage/index.html" width="350" height="150"></iframe>

## Fill color setting

A Fill color will be set by `color` argument, and this is required one. If you want to clear fill color, then specify a blank string to this argument.

For example, since the following code will clear fill color setting, so A result rectangle is invisible.

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

sprite.graphics.begin_fill(color='#0af')

# Clear fill color by specifying blank string.
sprite.graphics.begin_fill(color='')

# Since fill color is not set, the rectangle is invisible.
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

save_expressions_overall_html(
    dest_dir_path='graphics_begin_fill_color_setting_clear/')
```

<iframe src="static/graphics_begin_fill_color_setting_clear/index.html" width="150" height="150"></iframe>



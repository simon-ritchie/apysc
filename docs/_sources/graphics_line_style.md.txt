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

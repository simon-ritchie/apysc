# Graphics

This page will explain the `Graphics` class.

## What is Graphics

The `Graphics` is the class to handle each vector graphics interface. This interface has the draw rectangle interface, draw line interface, or something else.

This class instance is instantiated by the `Sprite` or other `DisplayObject` instances.

## Call interfaces from sprite instance

Sprite (object container) instance has the `graphics` attribute so with this attribute, each drawing interface can be called.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=180,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)

# Draw the white border and cyan color rectangle.
sprite.graphics.line_style(color='#fff', thickness=5)
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Draw the magenta color polyline.
sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(color='#f0a', thickness=5)
sprite.graphics.move_to(x=150, y=50)
sprite.graphics.line_to(x=200, y=50)
sprite.graphics.line_to(x=150, y=100)
sprite.graphics.line_to(x=200, y=100)

# Draw the dashed line.
sprite.graphics.draw_dashed_line(
    x_start=50, y_start=130, x_end=200, y_end=130,
    dash_size=10, space_size=5)

save_expressions_overall_html(
    dest_dir_path='graphics_call_interfaces_from_sprite_instance/')
```

<iframe src="static/graphics_call_interfaces_from_sprite_instance/index.html" width="250" height="180"></iframe>

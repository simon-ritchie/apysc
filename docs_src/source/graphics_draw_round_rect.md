# Graphics draw_round_rect interface

This page will explain the `Graphics` class `draw_round_rect` method interface.

## What interface is this?

`draw_round_rect` interface will draw vector rounded rectangle graphics.

## Basic usage

`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates setting, and `width` and `height` will determine rectangle size.

This interface also has `ellipse_width` and `ellipse_height` arguments to set the round size to the rectangle corners.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

# Set 10-pixel ellipse size and draw the rectangle.
sprite.graphics.draw_round_rect(
    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)

# Set 20-pixel ellipse size and draw the rectangle.
sprite.graphics.draw_round_rect(
    x=150, y=50, width=50, height=50, ellipse_width=20, ellipse_height=20)

# Set 5-pixel ellipse width and 20-pixel ellipse height and
# draw the rectangle.
sprite.graphics.draw_round_rect(
    x=250, y=50, width=50, height=50, ellipse_width=5, ellipse_height=20)

save_overall_html(
    dest_dir_path='graphics_draw_round_rect_basic_usage/')
```

<iframe src="static/graphics_draw_round_rect_basic_usage/index.html" width="350" height="150"></iframe>

## Return value

`draw_round_rect` interface will return the `Rectangle` instance, same as the `draw_rect` interface.

`Rectangle` instance has `ellipse_size`, `ellipse_width`, and `ellipse_height` attributes to change the rectangle round size (`ellipse_size` will change both `width` and `height` by the same size).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import Int
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

rectangle: Rectangle = sprite.graphics.draw_round_rect(
    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)

# You can update the ellipse_width and ellipse_height
# attributes dynamically.
rectangle.ellipse_width = Int(20)

save_overall_html(
    dest_dir_path='graphics_draw_round_rect_return_value/')
```

<iframe src="static/graphics_draw_round_rect_return_value/index.html" width="150" height="150"></iframe>

# Graphics draw_circle interface

This page will explain the `Graphics` class `draw_circle` method interface.

## What interface is this?

`draw_circle` interface will draw vector circle graphics.

## Basic usage

`draw_circle` interface has `x`, `y`, and `radius` interfaces. `x` and `y` are the circle center coordinates. The circle width and height will be twice the `radius`.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineDotSetting
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=350,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)

# Set the cyan color and draw the circle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_circle(x=100, y=100, radius=100)

# Set the dotted-line style and draw the circle.
sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(
    color='#fff', thickness=3, dot_setting=LineDotSetting(dot_size=3))
sprite.graphics.draw_circle(x=250, y=100, radius=100)

# Draw the inner circle.
sprite.graphics.draw_circle(x=250, y=100, radius=50)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_circle_basic_usage/')
```

<iframe src="static/graphics_draw_circle_basic_usage/index.html" width="350" height="200"></iframe>

## Return value

The return value of the `draw_circle` interface is the instance of the `Circle` class.

It has the `radius` attribute or other basic interfaces and you can change these settings.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import Circle
from apysc import Int
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=400,
    stage_height=400,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)

# Draw the small radius circle.
sprite.graphics.begin_fill(color='#0af')
circle: Circle = sprite.graphics.draw_circle(x=200, y=200, radius=30)

# Update circle radius to become the bigger one.
circle.radius = Int(150)

save_expressions_overall_html(
    dest_dir_path='graphics_draw_circle_return_value/')
```

<iframe src="static/graphics_draw_circle_return_value/index.html" width="400" height="400"></iframe>

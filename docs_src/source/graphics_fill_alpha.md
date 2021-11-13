# Graphics fill_alpha interface

This page will explain the `Graphics` class `fill_alpha` property interface.

## What interface is this?

The `fill_alpha` property interface will update or get the instance's fill alpha (opacity).

## Basic usage

The getter and setter interface will be (or require) the `Number` value (0.0 to 1.0).

The following example will set the 0.5 fill alpha to the second rectangle and 0.25 to the third rectangle:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.fill_alpha = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)
rectangle_3.fill_alpha = ap.Number(0.25)

ap.save_overall_html(
    dest_dir_path='./graphics_fill_alpha_basic_usage/')
```

<iframe src="static/graphics_fill_alpha_basic_usage/index.html" width="350" height="150"></iframe>

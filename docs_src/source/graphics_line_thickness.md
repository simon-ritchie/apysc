# Graphics line_thickness interface

This page will explain the `Graphics` class `line_thickness` property interface.

## What interface is this?

The `line_thickness` property interface will update or get the instance's line thickness (line width).

## Basic usage

The getter or setter interface will be (or require) the `Int` value.

The following example will set the 5-pixel line thickness to the first rectangle and the 10-pixel line thickness to the second one:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.line_style(color='#0af', thickness=1)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_1.line_thickness = ap.Int(5)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='./graphics_line_thickness_basic_usage/')
```

<iframe src="static/graphics_line_thickness_basic_usage/index.html" width="250" height="150"></iframe>

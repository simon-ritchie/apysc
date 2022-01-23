# Graphics line_alpha interface

This page explains the `Graphics` class `line_alpha` property interface.

## What interface is this?

The `line_alpha` property interface updates or get the instance's line alpha (opacity).

## Basic usage

The getter or setter interface value becomes (or requires) the `Number` value (0.0 to 1.0).

The following example sets the 0.5 line alpha to the second rectangle and 0.25 to the third rectangle:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=5)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.line_alpha = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)
rectangle_3.line_alpha = ap.Number(0.25)

ap.save_overall_html(
    dest_dir_path='./graphics_line_alpha_basic_usage/')
```

<iframe src="static/graphics_line_alpha_basic_usage/index.html" width="350" height="150"></iframe>
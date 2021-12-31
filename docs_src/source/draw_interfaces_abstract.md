# Draw interfaces abstract

This page would explain the drawing interfaces abstract.

## What apysc can do in its drawing interfaces

- You can set the fill-color, fill-alpha (opacity), line-color, line-alpha, line-thickness values and draw each SVG graphic with these.
- Supported graphics: The rectangle, circle, ellipse, polygon, line, polyline, and path.

## Fill settings

The `begin_fill` interface sets the fill-color and fill-alpha (opacity).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af', alpha=0.5)
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='draw_interfaces_abstract_begin_fill/')
```

<iframe src="static/draw_interfaces_abstract_begin_fill/index.html" width="150" height="150"></iframe>

For more details, please see the [Graphics class begin fill interface](graphics_begin_fill.md).

## Line style settings

The `line_style` interface sets the line-color, line-alpha (opacity), line-thickness.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=5, alpha=0.5)
sprite.graphics.draw_line(x_start=50, y_start=50, x_end=150, y_end=50)

ap.save_overall_html(
    dest_dir_path='draw_interfaces_abstract_line_style/')
```

<iframe src="static/draw_interfaces_abstract_line_style/index.html" width="200" height="100"></iframe>

For more details, please see the [Graphics class line style interface](graphics_line_style.md).

## Each drawing interface

Each drawing interface has the `draw_` prefix draw SVG graphics (e.g., draw_rect, draw_circle).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_circle(x=175, y=75, radius=25)

ap.save_overall_html(
    dest_dir_path='draw_interfaces_abstract_each_drawing_interface/')
```

<iframe src="static/draw_interfaces_abstract_each_drawing_interface/index.html" width="250" height="150"></iframe>

For more details, please see the following:

- [Graphics class draw rect interface](graphics_draw_rect.md)
- [Graphics class draw round rect interface](graphics_draw_round_rect.md)
- [Graphics class draw circle interface](graphics_draw_circle.md)
- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)
- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)
- [Graphics class draw line interface](graphics_draw_line.md)
- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)
- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)
- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)
- [Graphics class draw polygon interface](graphics_draw_polygon.md)

## See also

- [Graphics class](graphics.md)
- [Graphics class fill color interface](graphics_fill_color.md)
- [Graphics class fill alpha interface](graphics_fill_alpha.md)
- [Graphics class line color interface](graphics_line_color.md)
- [Graphics class line alpha interface](graphics_line_alpha.md)
- [Graphics class line thickness interface](graphics_line_thickness.md)
- [Graphics class line dot setting interface](graphics_line_dot_setting.md)
- [Graphics class line dash setting interface](graphics_line_dash_setting.md)
- [Graphics class line round dot setting interface](graphics_line_round_dot_setting.md)
- [Graphics class line dash dot setting interface](graphics_line_dash_dot_setting.md)

# Graphics line_dash_setting interface

This page explains the `Graphics` class `line_dash_setting` property interface.

## What interface is this?

The `line_dash_setting` property interface updates or gets the instance's current line dash setting.

## Basic usage

The getter or setter interface becomes (or requires) the `LineDashSetting` instance value.

The following example sets the 10-pixel dash size and 3-pixel space size to the line:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=100, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=5)

line: ap.Line = sprite.graphics.draw_line(
    x_start=50, y_start=50, x_end=200, y_end=50)
line.line_dash_setting = ap.LineDashSetting(dash_size=10, space_size=3)

ap.save_overall_html(
    dest_dir_path='./graphics_line_dash_setting_basic_usage/')
```

<iframe src="static/graphics_line_dash_setting_basic_usage/index.html" width="250" height="100"></iframe>

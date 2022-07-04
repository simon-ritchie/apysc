# Line class

This page explains the `Line` class.

## What class is this?

The `Line` class creates a straight-line vector graphics object.

## Basic usage

The `Line` class constructor requires the `start_point` and `end_point` arguments.

The constructor also accepts each style's argument, such as the `line_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)

ap.save_overall_html(
    dest_dir_path='line_basic_usage/')
```

<iframe src="static/line_basic_usage/index.html" width="200" height="100"></iframe>

## Note of the draw_line or other interfaces

You can also create a line instance with the `draw_line` interface (or the other interfaces, such as the `draw_dotted_line`).

Please see also:

- [Graphics class draw_line interface](graphics_draw_line.md)
- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)
- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)
- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)
line.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='line_x/')
```

<iframe src="static/line_x/index.html" width="200" height="100"></iframe>

Notes: this attribute's value becomes the same as the arguments' minimum point value.

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)
line.y = ap.Int(80)

ap.save_overall_html(
    dest_dir_path='line_y/')
```

<iframe src="static/line_y/index.html" width="200" height="100"></iframe>

Notes: this attribute's value becomes the same as the arguments' minimum point value.

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50), line_thickness=5)
line.line_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='line_line_color/')
```

<iframe src="static/line_line_color/index.html" width="200" height="100"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=5)
line.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='line_line_alpha/')
```

<iframe src="static/line_line_alpha/index.html" width="200" height="100"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af')
line.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='line_line_thickness/')
```

<iframe src="static/line_line_thickness/index.html" width="200" height="100"></iframe>

## line_dot_setting property interface example

The `line_dot_setting` property updates or gets the instance's line dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=3)
line.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='line_line_dot_setting/')
```

<iframe src="static/line_line_dot_setting/index.html" width="200" height="100"></iframe>

## line_dash_setting property interface example

The `line_dash_setting` property updates or gets the instance's line dash-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=3)
line.line_dash_setting = ap.LineDashSetting(
    dash_size=6, space_size=2)

ap.save_overall_html(
    dest_dir_path='line_line_dash_setting/')
```

<iframe src="static/line_line_dash_setting/index.html" width="200" height="100"></iframe>

## line_round_dot_setting property interface example

The `line_round_dot_setting` property updates or gets the instance's line round dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af')
line.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=3)

ap.save_overall_html(
    dest_dir_path='line_line_round_dot_setting/')
```

<iframe src="static/line_line_round_dot_setting/index.html" width="200" height="100"></iframe>

## line_dash_dot_setting property interface example

The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=50),
    end_point=ap.Point2D(x=150, y=50),
    line_color='#0af', line_thickness=3)
line.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=2, dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='line_line_dash_dot_setting/')
```

<iframe src="static/line_line_dash_dot_setting/index.html" width="200" height="100"></iframe>
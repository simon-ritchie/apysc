# Circle class

This page explains the `Circle` class.

## What class is this?

The `Circle` class creates a circle vector graphics object.

## Basic usage

The `Circle` class constructor requires the `x` (center-x), `y` (center-y), and `radius` arguments.

The constructor also accepts each style's argument, such as the `fill_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='circle_basic_usage/')
```

<iframe src="static/circle_basic_usage/index.html" width="150" height="150"></iframe>

## Note of the draw_circle interface

You can also create a circle instance with the `draw_circle` interface.

Please see also:

- [Graphics class draw_circle interface](graphics_draw_circle.md)

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=0, y=75, radius=50, fill_color='#0af')
circle.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='circle_x/')
```

<iframe src="static/circle_x/index.html" width="200" height="150"></iframe>

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=0, radius=50, fill_color='#0af')
circle.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='circle_y/')
```

<iframe src="static/circle_y/index.html" width="150" height="200"></iframe>

## radius property interface example

The `radius` property updates or gets the instance's radius:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=0, fill_color='#0af')
circle.radius = ap.Int(30)

ap.save_overall_html(
    dest_dir_path='circle_radius/')
```

<iframe src="static/circle_radius/index.html" width="150" height="150"></iframe>

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50)
circle.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='circle_fill_color/')
```

<iframe src="static/circle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, fill_color='#0af')
circle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='circle_fill_alpha/')
```

<iframe src="static/circle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_thickness=5)
circle.line_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='circle_line_color/')
```

<iframe src="static/circle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=5)
circle.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='circle_line_alpha/')
```

<iframe src="static/circle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af')
circle.line_thickness = ap.Int(8)

ap.save_overall_html(
    dest_dir_path='circle_line_thickness/')
```

<iframe src="static/circle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting property interface example

The `line_dot_setting` property updates or gets the instance's line dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_dot_setting/')
```

<iframe src="static/circle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting property interface example

The `line_dash_setting` property updates or gets the instance's line dash-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dash_setting = ap.LineDashSetting(
    dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='circle_line_dash_setting/')
```

<iframe src="static/circle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting property interface example

The `line_round_dot_setting` property updates or gets the instance's line round dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af')
circle.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_round_dot_setting/')
```

<iframe src="static/circle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting property interface example

The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
circle: ap.Circle = ap.Circle(
    x=75, y=75, radius=50, line_color='0af', line_thickness=3)
circle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='circle_line_dash_dot_setting/')
```

<iframe src="static/circle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>
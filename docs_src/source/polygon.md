# Polygon class

This page explains the `Polygon` class.

## What class is this?

The `Polygon` class creates a polygon vector graphics object.

## Basic usage

The `Polygon` class constructor requires the `points` list argument.

The constructor also accepts each style's argument, such as the `fill_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='polygon_basic_usage/')
```

<iframe src="static/polygon_basic_usage/index.html" width="150" height="150"></iframe>

## Note of the draw_polygon interface

You can also create a polygon instance with the `draw_polygon` interface.

Please see also:

- [Graphics class draw_polygon interface](graphics_draw_polygon.md)

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    fill_color='#0af')
polygon.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='polygon_x/')
```

<iframe src="static/polygon_x/index.html" width="150" height="150"></iframe>

Notes: this attribute's value becomes the same as the arguments' minimum point value.

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    fill_color='#0af')
polygon.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='polygon_y/')
```

<iframe src="static/polygon_y/index.html" width="150" height="150"></iframe>

Notes: this attribute's value becomes the same as the arguments' minimum point value.

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ])
polygon.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='polygon_fill_color/')
```

<iframe src="static/polygon_fill_color/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    fill_color='#0af')
polygon.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='polygon_fill_alpha/')
```

<iframe src="static/polygon_fill_alpha/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_thickness=5)
polygon.line_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='polygon_line_color/')
```

<iframe src="static/polygon_line_color/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_color='#0af',
    line_thickness=5)
polygon.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='polygon_line_alpha/')
```

<iframe src="static/polygon_line_alpha/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_color='#0af')
polygon.line_thickness = ap.Int(8)

ap.save_overall_html(
    dest_dir_path='polygon_line_thickness/')
```

<iframe src="static/polygon_line_thickness/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_color='#0af',
    line_thickness=2)
polygon.line_dot_setting = ap.LineDotSetting(dot_size=2)

ap.save_overall_html(
    dest_dir_path='polygon_line_dot_setting/')
```

<iframe src="static/polygon_line_dot_setting/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_color='#0af',
    line_thickness=2)
polygon.line_dash_setting = ap.LineDashSetting(
    dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='polygon_line_dash_setting/')
```

<iframe src="static/polygon_line_dash_setting/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_color='#0af')
polygon.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=4, space_size=3)

ap.save_overall_html(
    dest_dir_path='polygon_line_round_dot_setting/')
```

<iframe src="static/polygon_line_round_dot_setting/index.html" width="150" height="150"></iframe>

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
polygon: ap.Polygon = ap.Polygon(
    points=[
        ap.Point2D(x=75, y=50),
        ap.Point2D(x=50, y=100),
        ap.Point2D(x=100, y=100),
    ],
    line_color='#0af')
polygon.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=2, dash_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='polygon_line_dash_dot_setting/')
```

<iframe src="static/polygon_line_dash_dot_setting/index.html" width="150" height="150"></iframe>
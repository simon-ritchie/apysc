# Rectangle class

This page explains the `Rectangle` class.

## What class is this?

The `Rectangle` class creates a rectangle vector graphics object.

## Basic usage

The `Rectangle` class constructor requires the `x`, `y`, `width`, and `height` arguments.

The constructor also accepts each style's argument, such as the `fill_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=100, height=50,
    fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='rectangle_basic_usage/')
```

<iframe src="static/rectangle_basic_usage/index.html" width="200" height="150"></iframe>

## Note of the draw_rect interface

You can also create a rectangle instance with the `draw_rect` interface.

Please see also:

- [Graphics class draw_rect interface](graphics_draw_rect.md)

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=0, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_x/')
```

<iframe src="static/rectangle_x/index.html" width="200" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=0, width=50, height=50,
    fill_color='#0af')
rectangle.y = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_y/')
```

<iframe src="static/rectangle_y/index.html" width="150" height="200"></iframe>

## width property interface example

The `width` property updates or gets the instance's width:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.width = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_width/')
```

<iframe src="static/rectangle_width/index.html" width="200" height="150"></iframe>

## height property interface example

The `height` property updates or gets the instance's height:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.height = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='rectangle_height/')
```

<iframe src="static/rectangle_height/index.html" width="150" height="200"></iframe>

## ellipse_width property interface example

The `ellipse_width` property updates or gets the instance's ellipse width:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.ellipse_width = ap.Int(30)
rectangle.ellipse_height = ap.Int(15)

ap.save_overall_html(
    dest_dir_path='rectangle_ellipse_width/')
```

<iframe src="static/rectangle_ellipse_width/index.html" width="150" height="150"></iframe>

## ellipse_height property interface example

The `ellipse_height` property updates or gets the instance's ellipse height:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.ellipse_width = ap.Int(15)
rectangle.ellipse_height = ap.Int(30)

ap.save_overall_html(
    dest_dir_path='rectangle_ellipse_height/')
```

<iframe src="static/rectangle_ellipse_height/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='rectangle_fill_color/')
```

<iframe src="static/rectangle_fill_color/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    fill_color='#0af')
rectangle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='rectangle_fill_alpha/')
```

<iframe src="static/rectangle_fill_alpha/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_thickness=5)
rectangle.line_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='rectangle_line_color/')
```

<iframe src="static/rectangle_line_color/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=5)
rectangle.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_alpha/')
```

<iframe src="static/rectangle_line_alpha/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50, line_color='#0af')
rectangle.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='rectangle_line_thickness/')
```

<iframe src="static/rectangle_line_thickness/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=5)
rectangle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_dot_setting/')
```

<iframe src="static/rectangle_line_dot_setting/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=2)
rectangle.line_dash_setting = ap.LineDashSetting(
    dash_size=7, space_size=2)

ap.save_overall_html(
    dest_dir_path='rectangle_line_dash_setting/')
```

<iframe src="static/rectangle_line_dash_setting/index.html" width="150" height="150"></iframe>

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
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=5)
rectangle.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_round_dot_setting/')
```

<iframe src="static/rectangle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting property interface example

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
rectangle: ap.Rectangle = ap.Rectangle(
    x=50, y=50, width=50, height=50,
    line_color='#0af', line_thickness=3)
rectangle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=7, space_size=3)

ap.save_overall_html(
    dest_dir_path='rectangle_line_dash_dot_setting/')
```

<iframe src="static/rectangle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>
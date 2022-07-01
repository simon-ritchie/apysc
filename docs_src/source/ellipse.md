# Ellipse class

This page explains the `Ellipse` class.

## What class is this?

The `Ellipse` class creates an ellipse vector graphics object.

## Basic usage

The `Ellipse` class constructor requires the `x` (center-x), `y` (center-y), `width`, and `height` arguments.

The constructor also accepts each style's argument, such as the `fill_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, fill_color='#0af')

ap.save_overall_html(
    dest_dir_path='ellipse_basic_usage/')
```

<iframe src="static/ellipse_basic_usage/index.html" width="150" height="150"></iframe>

## Note of the draw_ellipse interface

You can also create an ellipse instance with the `draw_ellipse` interface.

Please see also:

- [Graphics class draw_ellipse interface](graphics_draw_ellipse.md)

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=0, y=75, width=100, height=75, fill_color='#0af')
ellipse.x = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='ellipse_x/')
```

<iframe src="static/ellipse_x/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=0, width=100, height=50, fill_color='#0af')
ellipse.y = ap.Int(125)

ap.save_overall_html(
    dest_dir_path='ellipse_y/')
```

<iframe src="static/ellipse_y/index.html" width="150" height="150"></iframe>

## width property interface example

The `width` property updates or gets the instance's width:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=0, height=75, fill_color='#0af')
ellipse.width = ap.Int(125)

ap.save_overall_html(
    dest_dir_path='ellipse_width/')
```

<iframe src="static/ellipse_width/index.html" width="150" height="150"></iframe>

## height property interface example

The `height` property updates or gets the instance's height:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=75, height=0, fill_color='#0af')
ellipse.height = ap.Int(125)

ap.save_overall_html(
    dest_dir_path='ellipse_height/')
```

<iframe src="static/ellipse_height/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75)
ellipse.fill_color = ap.String('#f0a')

ap.save_overall_html(
    dest_dir_path='ellipse_fill_color/')
```

<iframe src="static/ellipse_fill_color/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, fill_color='#0af')
ellipse.fill_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='ellipse_fill_alpha/')
```

<iframe src="static/ellipse_fill_alpha/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_thickness=5)
ellipse.line_color = ap.String('#0af')

ap.save_overall_html(
    dest_dir_path='ellipse_line_color/')
```

<iframe src="static/ellipse_line_color/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=5)
ellipse.line_alpha = ap.Number(0.3)

ap.save_overall_html(
    dest_dir_path='ellipse_line_alpha/')
```

<iframe src="static/ellipse_line_alpha/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_color='0af')
ellipse.line_thickness = ap.Int(8)

ap.save_overall_html(
    dest_dir_path='ellipse_line_thickness/')
```

<iframe src="static/ellipse_line_thickness/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=2)
ellipse.line_dot_setting = ap.LineDotSetting(dot_size=2)

ap.save_overall_html(
    dest_dir_path='ellipse_line_dot_setting/')
```

<iframe src="static/ellipse_line_dot_setting/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=2)
ellipse.line_dash_setting = ap.LineDashSetting(
    dash_size=6, space_size=2)

ap.save_overall_html(
    dest_dir_path='ellipse_line_dash_setting/')
```

<iframe src="static/ellipse_line_dash_setting/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75, line_color='0af')
ellipse.line_round_dot_setting = ap.LineRoundDotSetting(
    round_size=5, space_size=2)

ap.save_overall_html(
    dest_dir_path='ellipse_line_round_dot_setting/')
```

<iframe src="static/ellipse_line_round_dot_setting/index.html" width="150" height="150"></iframe>

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
ellipse: ap.Ellipse = ap.Ellipse(
    x=75, y=75, width=100, height=75,
    line_color='0af', line_thickness=2)
ellipse.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3)

ap.save_overall_html(
    dest_dir_path='ellipse_line_dash_dot_setting/')
```

<iframe src="static/ellipse_line_dash_dot_setting/index.html" width="150" height="150"></iframe>
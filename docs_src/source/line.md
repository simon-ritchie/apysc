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

## rotation_around_center property interface example

The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color='#0af',
    line_thickness=3)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    line.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='line_rotation_around_center/')
```

<iframe src="static/line_rotation_around_center/index.html" width="200" height="100"></iframe>

## set_rotation_around_point and get_rotation_around_point methods interfaces example

The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.

Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color='#0af',
    line_thickness=3)
x: ap.Int = ap.Int(100)
y: ap.Int = ap.Int(100)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rotation: ap.Int = line.get_rotation_around_point(
        x=x, y=y)
    rotation += 1
    line.set_rotation_around_point(
        rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='line_set_rotation_around_point/')
```

<iframe src="static/line_set_rotation_around_point/index.html" width="200" height="100"></iframe>

## flip_x property interface example

The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color='#0af',
    line_thickness=3)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    line.flip_x = line.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(
    dest_dir_path='line_flip_x/')
```

<iframe src="static/line_flip_x/index.html" width="200" height="100"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## flip_y property interface example

The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color='#0af',
    line_thickness=3)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    line.flip_y = line.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(
    dest_dir_path='line_flip_y/')
```

<iframe src="static/line_flip_y/index.html" width="200" height="100"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## skew_x property interface example

The `skew_x` property updates or gets the instance's skew-x (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color='#0af',
    line_thickness=3)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    line.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='line_skew_x/')
```

<iframe src="static/line_skew_x/index.html" width="200" height="100"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## skew_y property interface example

The `skew_y` property updates or gets the instance's skew-y (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=100,
    stage_elem_id='stage')
line: ap.Line = ap.Line(
    start_point=ap.Point2D(x=50, y=40),
    end_point=ap.Point2D(x=150, y=60),
    line_color='#0af',
    line_thickness=3)


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    line.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(
    dest_dir_path='line_skew_y/')
```

<iframe src="static/line_skew_y/index.html" width="200" height="100"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## Line class constructor API

<!-- Docstring: apysc._display.line.Line.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, start_point: 'point2d.Point2D', end_point: 'point2d.Point2D', line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_interface.ChildInterface, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]** Create a line vector graphic.<hr>

**[Parameters]**

- `start_point`: Points2D
  - Line start point.
- `end_point`: Points2D
  - Line end point.
- `line_color`: str or String, default ''
  - A line-color to set.
- `line_alpha`: float or Number, default 1.0
  - A line-alpha to set.
- `line_thickness`: int or Int, default 1
  - A line-thickness (line-width) to set.
- `line_cap`: String or LineCaps or None, default None
  - A line-cap setting to set.
- `line_dot_setting`: LineDotSetting or None, default None
  - A dot setting to set.
- `line_dash_setting`: LineDashSetting or None, default None
  - A dash setting to set.
- `line_round_dot_setting`: LineRoundDotSetting or None, default None
  - A round-dot setting to set.
- `line_dash_dot_setting`: LineDashDotSetting or None, default None
  - A dash dot (1-dot chain) setting to set.
- `parent`: ChildInterface or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> line: ap.Line = ap.Line(
...    start_point=ap.Point2D(x=50, y=50),
...    end_point=ap.Point2D(x=150, y=50),
...    line_color='#ffffff',
...    line_thickness=3)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(3)
```
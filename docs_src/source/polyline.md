# Polyline class

This page explains the `Polyline` class.

## What class is this?

The `Polyline` class creates a polyline vector graphics object.

## Basic usage

The `Polyline` class constructor requires the `points` list argument.

The constructor also accepts each style's argument, such as the `line_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="polyline_basic_usage/")
```

<iframe src="static/polyline_basic_usage/index.html" width="200" height="150"></iframe>

## Note of the move_to and line_to interfaces

You can also create a polyline instance with the `move_to` and `line_to` interfaces.

Please see also:

- [Graphics class move_to and line_to interfaces](graphics_move_to_and_line_to.md)

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
polyline.x = ap.Int(100)

ap.save_overall_html(dest_dir_path="polyline_x/")
```

<iframe src="static/polyline_x/index.html" width="200" height="150"></iframe>

Notes: This attribute's value becomes the same as the arguments' minimum point value.

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
polyline.y = ap.Int(100)

ap.save_overall_html(dest_dir_path="polyline_y/")
```

<iframe src="static/polyline_y/index.html" width="200" height="150"></iframe>

Notes: This attribute's value becomes the same as the arguments' minimum point value.

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#fff",
    line_thickness=3,
)
polyline.fill_color = ap.String("#0af")

ap.save_overall_html(dest_dir_path="polyline_fill_color/")
```

<iframe src="static/polyline_fill_color/index.html" width="200" height="150"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    fill_color="#0af",
    line_color="#fff",
    line_thickness=3,
)
polyline.fill_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="polyline_fill_alpha/")
```

<iframe src="static/polyline_fill_alpha/index.html" width="200" height="150"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_thickness=3,
)
polyline.line_color = ap.String("#0af")

ap.save_overall_html(dest_dir_path="polyline_line_color/")
```

<iframe src="static/polyline_line_color/index.html" width="200" height="150"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
polyline.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="polyline_line_alpha/")
```

<iframe src="static/polyline_line_alpha/index.html" width="200" height="150"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
)
polyline.line_thickness = ap.Int(6)

ap.save_overall_html(dest_dir_path="polyline_line_thickness/")
```

<iframe src="static/polyline_line_thickness/index.html" width="200" height="150"></iframe>

## line_dot_setting property interface example

The `line_dot_setting` property updates or gets the instance's line dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
polyline.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="polyline_line_dot_setting/")
```

<iframe src="static/polyline_line_dot_setting/index.html" width="200" height="150"></iframe>

## line_dash_setting property interface example

The `line_dash_setting` property updates or gets the instance's line dash-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
polyline.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)

ap.save_overall_html(dest_dir_path="polyline_line_dash_setting/")
```

<iframe src="static/polyline_line_dash_setting/index.html" width="200" height="150"></iframe>

## line_round_dot_setting property interface example

The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
)
polyline.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)

ap.save_overall_html(dest_dir_path="polyline_line_round_dot_setting/")
```

<iframe src="static/polyline_line_round_dot_setting/index.html" width="200" height="150"></iframe>

## line_dash_dot_setting property interface example

The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
polyline.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=2, dash_size=5, space_size=2
)

ap.save_overall_html(dest_dir_path="polyline_line_dash_dot_setting/")
```

<iframe src="static/polyline_line_dash_dot_setting/index.html" width="200" height="150"></iframe>

## rotation_around_center property interface example

The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)


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
    polyline.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_rotation_around_center/")
```

<iframe src="static/polyline_rotation_around_center/index.html" width="200" height="150"></iframe>

## set_rotation_around_point and get_rotation_around_point methods interfaces example

The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.

Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
x: ap.Int = ap.Int(150)
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
    rotation: ap.Int = polyline.get_rotation_around_point(x=x, y=y)
    rotation += 1
    polyline.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_set_rotation_around_point/")
```

<iframe src="static/polyline_set_rotation_around_point/index.html" width="200" height="150"></iframe>

## scale_x_from_center property interface example

The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(-1)


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
    with ap.If(polyline.scale_x_from_center <= 0.001):
        direction.value = 1
    with ap.If(polyline.scale_x_from_center >= 2.0):
        direction.value = -1
    polyline.scale_x_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_scale_x_from_center/")
```

<iframe src="static/polyline_scale_x_from_center/index.html" width="200" height="150"></iframe>

## scale_y_from_center property interface example

The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(-1)


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
    with ap.If(polyline.scale_y_from_center <= 0.001):
        direction.value = 1
    with ap.If(polyline.scale_y_from_center >= 2.0):
        direction.value = -1
    polyline.scale_y_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_scale_y_from_center/")
```

<iframe src="static/polyline_scale_y_from_center/index.html" width="200" height="150"></iframe>

## set_scale_x_from_point and get_scale_x_from_point methods interfaces example

The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.

Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(-1)
x: ap.Int = ap.Int(150)


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
    scale: ap.Number = polyline.get_scale_x_from_point(x=x)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    polyline.set_scale_x_from_point(scale_x=scale, x=x)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_scale_x_from_point/")
```

<iframe src="static/polyline_scale_x_from_point/index.html" width="200" height="150"></iframe>

## set_scale_y_from_point and get_scale_y_from_point methods interfaces example

The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.

Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=100, y=100),
        ap.Point2D(x=150, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(-1)
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
    scale: ap.Number = polyline.get_scale_y_from_point(y=y)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    polyline.set_scale_y_from_point(scale_y=scale, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_scale_y_from_point/")
```

<iframe src="static/polyline_scale_y_from_point/index.html" width="200" height="150"></iframe>

## flip_x property interface example

The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=50, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)


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
    polyline.flip_x = polyline.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="polyline_flip_x/")
```

<iframe src="static/polyline_flip_x/index.html" width="150" height="150"></iframe>

## flip_y property interface example

The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=50, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)


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
    polyline.flip_y = polyline.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="polyline_flip_y/")
```

<iframe src="static/polyline_flip_y/index.html" width="150" height="150"></iframe>

## skew_x property interface example

The `skew_x` property updates or gets the instance's skew-x (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=50, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)


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
    polyline.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_skew_x/")
```

<iframe src="static/polyline_skew_x/index.html" width="150" height="150"></iframe>

## skew_y property interface example

The `skew_y` property updates or gets the instance's skew-y (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
polyline: ap.Polyline = ap.Polyline(
    points=[
        ap.Point2D(x=50, y=50),
        ap.Point2D(x=100, y=50),
        ap.Point2D(x=50, y=100),
    ],
    line_color="#0af",
    line_thickness=3,
)


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
    polyline.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="polyline_skew_y/")
```

<iframe src="static/polyline_skew_y/index.html" width="150" height="150"></iframe>

## Polyline class constructor API

<!-- Docstring: apysc._display.polyline.Polyline.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, points: Union[apysc._type.array.Array[apysc._geom.point2d.Point2D], List[apysc._geom.point2d.Point2D]], fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Create a polyline vector graphic.<hr>

**[Parameters]**

- `points`: Array of Point2D or list of Point2D
  - List of line points.
- `fill_color`: str or String, default ''
  - A fill-color to set.
- `fill_alpha`: float or Number, default 1.0
  - A fill-alpha to set.
- `line_color`: str or String, default ''
  - A line-color to set.
- `line_alpha`: float or Number, default 1.0
  - A line-alpha to set.
- `line_thickness`: int or Int, default 1
  - A line-thickness (line-width) to set.
- `line_cap`: String or LineCaps or None, default None
  - A line-cap setting to set.
- `line_joints`: String or LineJoints or None, default None
  - A line-joints setting to set.
- `line_dot_setting`: LineDotSetting or None, default None
  - A dot setting to set.
- `line_dash_setting`: LineDashSetting or None, default None
  - A dash setting to set.
- `line_round_dot_setting`: LineRoundDotSetting or None, default None
  - A round-dot setting to set.
- `line_dash_dot_setting`: LineDashDotSetting or None, default None
  - A dash dot (1-dot chain) setting to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> polyline: ap.Polyline = ap.Polyline(
...     points=[
...         ap.Point2D(x=50, y=50),
...         ap.Point2D(x=100, y=100),
...         ap.Point2D(x=150, y=50),
...     ],
...     line_color="#ffffff",
...     line_thickness=3,
... )
>>> polyline.line_color
String('#ffffff')

>>> polyline.line_thickness
Int(3)
```
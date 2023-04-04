# Circle class

This page explains the `Circle` class.

## What class is this?

The `Circle` class creates a circle vector graphics object.

## Basic usage

The `Circle` class constructor requires the `x` (center x), `y` (center y), and `radius` arguments.

The constructor also accepts each style's argument, such as the `fill_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")

ap.save_overall_html(dest_dir_path="circle_basic_usage/")
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
    background_color="#333", stage_width=200, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=0, y=75, radius=50, fill_color="#0af")
circle.x = ap.Number(100)

ap.save_overall_html(dest_dir_path="circle_x/")
```

<iframe src="static/circle_x/index.html" width="200" height="150"></iframe>

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=200, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=0, radius=50, fill_color="#0af")
circle.y = ap.Number(100)

ap.save_overall_html(dest_dir_path="circle_y/")
```

<iframe src="static/circle_y/index.html" width="150" height="200"></iframe>

## radius property interface example

The `radius` property updates or gets the instance's radius:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=0, fill_color="#0af")
circle.radius = ap.Int(30)

ap.save_overall_html(dest_dir_path="circle_radius/")
```

<iframe src="static/circle_radius/index.html" width="150" height="150"></iframe>

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50)
circle.fill_color = ap.String("#f0a")

ap.save_overall_html(dest_dir_path="circle_fill_color/")
```

<iframe src="static/circle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
circle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="circle_fill_alpha/")
```

<iframe src="static/circle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_thickness=5)
circle.line_color = ap.String("#f0a")

ap.save_overall_html(dest_dir_path="circle_line_color/")
```

<iframe src="static/circle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_color="0af", line_thickness=5)
circle.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="circle_line_alpha/")
```

<iframe src="static/circle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_color="0af")
circle.line_thickness = ap.Int(8)

ap.save_overall_html(dest_dir_path="circle_line_thickness/")
```

<iframe src="static/circle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting property interface example

The `line_dot_setting` property updates or gets the instance's line dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_color="0af", line_thickness=3)
circle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="circle_line_dot_setting/")
```

<iframe src="static/circle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting property interface example

The `line_dash_setting` property updates or gets the instance's line dash-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_color="0af", line_thickness=3)
circle.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)

ap.save_overall_html(dest_dir_path="circle_line_dash_setting/")
```

<iframe src="static/circle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting property interface example

The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_color="0af")
circle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=3)

ap.save_overall_html(dest_dir_path="circle_line_round_dot_setting/")
```

<iframe src="static/circle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting property interface example

The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, line_color="0af", line_thickness=3)
circle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3
)

ap.save_overall_html(dest_dir_path="circle_line_dash_dot_setting/")
```

<iframe src="static/circle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center property interface example

The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
circle.scale_x_from_center = ap.Number(0.5)


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
    circle.rotation_around_center += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_rotation_around_center/")
```

<iframe src="static/circle_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_point and get_rotation_around_point methods interface example

The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.

Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
circle.scale_x_from_center = ap.Number(0.5)
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
    rotation: ap.Int = circle.get_rotation_around_point(x=x, y=y)
    rotation += 1
    circle.set_rotation_around_point(rotation=rotation, x=x, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_set_rotation_around_point/")
```

<iframe src="static/circle_set_rotation_around_point/index.html" width="150" height="150"></iframe>

## scale_x_from_center property interface example

The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
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
    with ap.If(circle.scale_x_from_center <= 0.001):
        direction.value = 1
    with ap.If(circle.scale_x_from_center >= 2.0):
        direction.value = -1
    circle.scale_x_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_scale_x_from_center/")
```

<iframe src="static/circle_scale_x_from_center/index.html" width="150" height="150"></iframe>

## scale_y_from_center property interface example

The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
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
    with ap.If(circle.scale_y_from_center <= 0.001):
        direction.value = 1
    with ap.If(circle.scale_y_from_center >= 2.0):
        direction.value = -1
    circle.scale_y_from_center += direction * 0.005


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_scale_y_from_center/")
```

<iframe src="static/circle_scale_y_from_center/index.html" width="150" height="150"></iframe>

## set_scale_x_from_point and get_scale_x_from_point methods interface example

The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.

Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
direction: ap.Int = ap.Int(-1)
x: ap.Int = ap.Int(125)


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
    scale: ap.Number = circle.get_scale_x_from_point(x=x)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    circle.set_scale_x_from_point(scale_x=scale, x=x)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_scale_x_from_point/")
```

<iframe src="static/circle_scale_x_from_point/index.html" width="150" height="150"></iframe>

## set_scale_y_from_point and get_scale_y_from_point methods interface example

The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.

Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
direction: ap.Int = ap.Int(-1)
y: ap.Int = ap.Int(125)


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
    scale: ap.Number = circle.get_scale_y_from_point(y=y)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    scale += direction * 0.005
    circle.set_scale_y_from_point(scale_y=scale, y=y)


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_scale_y_from_point/")
```

<iframe src="static/circle_scale_y_from_point/index.html" width="150" height="150"></iframe>

## flip_x property interface example

The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
circle.scale_x_from_center = ap.Number(0.5)
circle.rotation_around_center = ap.Int(30)


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
    circle.flip_x = circle.flip_x.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="circle_flip_x/")
```

<iframe src="static/circle_flip_x/index.html" width="150" height="150"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## flip_y property interface example

The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")
circle.scale_x_from_center = ap.Number(0.5)
circle.rotation_around_center = ap.Int(30)


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
    circle.flip_y = circle.flip_y.not_


ap.Timer(on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="circle_flip_y/")
```

<iframe src="static/circle_flip_y/index.html" width="150" height="150"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## skew_x property interface example

The `skew_x` property updates or gets the instance's skew-x (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")


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
    circle.skew_x += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_skew_x/")
```

<iframe src="static/circle_skew_x/index.html" width="150" height="150"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## skew_y property interface example

The `skew_y` property updates or gets the instance's skew-y (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
circle: ap.Circle = ap.Circle(x=75, y=75, radius=50, fill_color="#0af")


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
    circle.skew_y += 1


ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="circle_skew_y/")
```

<iframe src="static/circle_skew_y/index.html" width="150" height="150"></iframe>

Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.

## Circle class constructor API

<!-- Docstring: apysc._display.circle.Circle.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], radius: Union[int, apysc._type.int.Int], fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Create a circle vector graphic.<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the circle center.
- `y`: float or Number
  - Y-coordinate of the circle center.
- `radius`: Int or int
  - Circle radius.
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
- `line_dot_setting`: LineDotSetting or None, default None
  - A dot setting to set.
- `line_dash_setting`: LineDashSetting or None, default None
  - A dash setting to set.
- `line_round_dot_setting`: LineRoundDotSetting or None, default None
  - A round-dot setting to set.
- `line_dash_dot_setting`: LineDashDotSetting or None, default None
  - A dash-dot (1-dot chain) setting to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> circle: ap.Circle = ap.Circle(x=100, y=100, radius=50, fill_color="#00aaff")
>>> circle.x
Number(100.0)

>>> circle.y
Number(100.0)

>>> circle.radius
Int(50)

>>> circle.fill_color
String("#00aaff")

>>> circle = ap.Circle(
...     x=100,
...     y=100,
...     radius=50,
...     line_color="#ffffff",
...     line_thickness=3,
...     line_dot_setting=ap.LineDotSetting(dot_size=10),
... )
>>> circle.line_color
String("#ffffff")

>>> circle.line_thickness
Int(3)
```
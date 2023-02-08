# Triangle class

This page explains the `Triangle` class.

## What class is this?

The `Triangle` class creates a triangle vector graphics object.

## Basic usage

The `Triangle` class constructor requires the `x1`, `y1`, `x2`, `y2`, `x3`, and `y3` arguments.

The `x1` and `y1` arguments are the first vertex's coordinates.

Similarly, the `x2` and `y2` are the second vertex's coordinates, and the `x3` and `y3` are the third.

The constructor also accepts each style's argument, such as the `fill_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)

ap.save_overall_html(dest_dir_path="triangle_basic_usage/")
```

<iframe src="static/triangle_basic_usage/index.html" width="150" height="150"></iframe>

## Note of the draw_triangle interface

you can also create a triangle instance with the `draw_triangle` interface.

For more details, please see the following:

- [Graphics draw_triangle interface](graphics_draw_triangle.md)

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x = ap.Number(100)

ap.save_overall_html(dest_dir_path="triangle_x/")
```

<iframe src="static/triangle_x/index.html" width="150" height="150"></iframe>

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y = ap.Number(100)

ap.save_overall_html(dest_dir_path="triangle_y/")
```

<iframe src="static/triangle_y/index.html" width="150" height="150"></iframe>

## x1 property interface example

The `x1` property updates or gets the instance's first vertex x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x1 = ap.Number(100)

ap.save_overall_html(dest_dir_path="triangle_x1/")
```

<iframe src="static/triangle_x1/index.html" width="150" height="150"></iframe>

## y1 property interface example

The `y1` property updates or gets the instance's first vertex y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y1 = ap.Number(0)

ap.save_overall_html(dest_dir_path="triangle_y1/")
```

<iframe src="static/triangle_y1/index.html" width="150" height="150"></iframe>

## x2 property interface example

The `x2` property updates or gets the instance's second vertex x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x2 = ap.Number(75)

ap.save_overall_html(dest_dir_path="triangle_x2/")
```

<iframe src="static/triangle_x2/index.html" width="150" height="150"></iframe>

## y2 property interface example

The `y2` property updates or gets the instance's second vertex y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y2 = ap.Number(75)

ap.save_overall_html(dest_dir_path="triangle_y2/")
```

<iframe src="static/triangle_y2/index.html" width="150" height="150"></iframe>

## x3 property interface example

The `x3` property updates or gets the instance's third vertex x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.x3 = ap.Number(75)

ap.save_overall_html(dest_dir_path="triangle_x3/")
```

<iframe src="static/triangle_x3/index.html" width="150" height="150"></iframe>

## y3 property interface example

The `y3` property updates or gets the instance's third vertex y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.y3 = ap.Number(75)

ap.save_overall_html(dest_dir_path="triangle_y3/")
```

<iframe src="static/triangle_y3/index.html" width="150" height="150"></iframe>

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.fill_color = ap.String("#f0a")

ap.save_overall_html(dest_dir_path="triangle_fill_color/")
```

<iframe src="static/triangle_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
triangle.fill_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="triangle_fill_alpha/")
```

<iframe src="static/triangle_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
    line_thickness=3,
)
triangle.line_color = ap.String("#fff")

ap.save_overall_html(dest_dir_path="triangle_line_color/")
```

<iframe src="static/triangle_line_color/index.html" width="150" height="150"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=3,
)
triangle.line_alpha = ap.Number(0.3)

ap.save_overall_html(dest_dir_path="triangle_line_alpha/")
```

<iframe src="static/triangle_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=1,
)
triangle.line_thickness = ap.Int(5)

ap.save_overall_html(dest_dir_path="triangle_line_thickness/")
```

<iframe src="static/triangle_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting property interface example

The `line_dot_setting` property updates or gets the instance's line dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=5,
)
triangle.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="triangle_line_dot_setting/")
```

<iframe src="static/triangle_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting property interface example

The `line_dash_setting` property updates or gets the instance's line dash-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=5,
)
triangle.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)

ap.save_overall_html(dest_dir_path="triangle_line_dash_setting/")
```

<iframe src="static/triangle_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting property interface example

The `line_round_dot_setting` property updates or gets the instance's line-round dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
)
triangle.line_round_dot_setting = ap.LineRoundDotSetting(round_size=6, space_size=3)

ap.save_overall_html(dest_dir_path="triangle_line_round_dot_setting/")
```

<iframe src="static/triangle_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting property interface example

The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    line_color="#0af",
    line_thickness=3,
)
triangle.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3, dash_size=6, space_size=3
)

ap.save_overall_html(dest_dir_path="triangle_line_dash_dot_setting/")
```

<iframe src="static/triangle_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center property interface example

The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle.rotation_around_center += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_rotation_around_center/")
```

<iframe src="static/triangle_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_point and get_rotation_around_point methods interfaces example

The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.

Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
ROTATION_X: ap.Int = ap.Int(100)
ROTATION_Y: ap.Int = ap.Int(100)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=ROTATION_X,
    y3=ROTATION_Y,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rotation: ap.Int = triangle.get_rotation_around_point(x=ROTATION_X, y=ROTATION_Y)
    triangle.set_rotation_around_point(
        rotation=rotation + 1, x=ROTATION_X, y=ROTATION_Y
    )


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_set_rotation_around_point/")
```

<iframe src="static/triangle_set_rotation_around_point/index.html" width="150" height="150"></iframe>

## scale_x_from_center property interface example

The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    with ap.If(triangle.scale_x_from_center <= 0.001):
        direction.value = 1
    with ap.If(triangle.scale_x_from_center >= 2.0):
        direction.value = -1
    triangle.scale_x_from_center += direction * 0.005


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_scale_x_from_center/")
```

<iframe src="static/triangle_scale_x_from_center/index.html" width="150" height="150"></iframe>

## scale_y_from_center property interface example

The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    with ap.If(triangle.scale_y_from_center <= 0.001):
        direction.value = 1
    with ap.If(triangle.scale_y_from_center >= 2.0):
        direction.value = -1
    triangle.scale_y_from_center += direction * 0.005


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_scale_y_from_center/")
```

<iframe src="static/triangle_scale_y_from_center/index.html" width="150" height="150"></iframe>

## set_scale_x_from_point and get_scale_x_from_point methods interfaces example

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
SCALE_COORDINATE_X: ap.Int = ap.Int(100)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=SCALE_COORDINATE_X,
    y3=100,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    scale: ap.Number = triangle.get_scale_x_from_point(x=SCALE_COORDINATE_X)
    scale += direction * 0.005
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    triangle.set_scale_x_from_point(scale_x=scale, x=SCALE_COORDINATE_X)


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_set_scale_x_from_point/")
```

<iframe src="static/triangle_set_scale_x_from_point/index.html" width="150" height="150"></iframe>

## set_scale_y_from_point and get_scale_y_from_point methods interfaces example

The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.

Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
SCALE_COORDINATE_Y: ap.Int = ap.Int(100)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=SCALE_COORDINATE_Y,
    fill_color="#0af",
)
direction: ap.Int = ap.Int(1)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    scale: ap.Number = triangle.get_scale_y_from_point(y=SCALE_COORDINATE_Y)
    scale += direction * 0.005
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2.0):
        direction.value = -1
    triangle.set_scale_y_from_point(scale_y=scale, y=SCALE_COORDINATE_Y)


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_set_scale_y_from_point/")
```

<iframe src="static/triangle_set_scale_y_from_point/index.html" width="150" height="150"></iframe>

## flip_x property interface example

The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=50,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
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
    triangle.flip_x = triangle.flip_x.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="triangle_flip_x/")
```

<iframe src="static/triangle_flip_x/index.html" width="150" height="150"></iframe>

## flip_y property interface example

The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
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
    triangle.flip_y = triangle.flip_y.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="triangle_flip_y/")
```

<iframe src="static/triangle_flip_y/index.html" width="150" height="150"></iframe>

## skew_x property interface example

The `skew_x` property updates or gets the instance's skew-x (distortion) value:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle.skew_x += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_skew_x/")
```

<iframe src="static/triangle_skew_x/index.html" width="150" height="150"></iframe>

## skew_y property interface example

The `skew_y` property updates or gets the instance's skew-y (distortion) value:

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
triangle: ap.Triangle = ap.Triangle(
    x1=75,
    y1=50,
    x2=50,
    y2=100,
    x3=100,
    y3=100,
    fill_color="#0af",
)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Triangle], options: dict) -> None:
    """
    The enter-frame event handler.

    Parameters
    ----------
    e : ap.EnterFrameEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    triangle.skew_y += 1


stage.enter_frame(handler=on_enter_frame)
ap.save_overall_html(dest_dir_path="triangle_skew_y/")
```

<iframe src="static/triangle_skew_y/index.html" width="150" height="150"></iframe>

## Triangle class constructor API

<!-- Docstring: apysc._display.triangle.Triangle.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, x1: Union[int, apysc._type.int.Int], y1: Union[int, apysc._type.int.Int], x2: Union[int, apysc._type.int.Int], y2: Union[int, apysc._type.int.Int], x3: Union[int, apysc._type.int.Int], y3: Union[int, apysc._type.int.Int], fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Create a triangle vector graphics instance.<hr>

**[Parameters]**

- `x1`: Union[int, Int]
  - First vertex's x coordinate.
- `y1`: Union[int, Int]
  - First vertex's y coordinate.
- `x2`: Union[int, Int]
  - Second vertex's x coordinate.
- `y2`: Union[int, Int]
  - Second vertex's y coordinate.
- `x3`: Union[int, Int]
  - Third vertex's x coordinate.
- `y3`: Union[int, Int]
  - Third vertex's y coordinate.
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
  - A dash-dot (1-dot chain) setting to set.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> triangle: ap.Triangle = ap.Triangle(
...     x1=75,
...     y1=50,
...     x2=50,
...     y2=100,
...     x3=100,
...     y3=100,
...     fill_color="#0af",
...     line_color="#fff",
...     line_thickness=3,
... )
>>> triangle.x2
Int(50)

>>> triangle.y1 = ap.Number(30)
>>> triangle.y1
Int(30.0)
```

## x1 property API

<!-- Docstring: apysc._display.polygon_x1_mixin.PolygonX1MixIn.x1 -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a first x-coordinate.<hr>

**[Returns]**

- `x1`: Int
  - A first x-coordinate.

## y1 property API

<!-- Docstring: apysc._display.polygon_y1_mixin.PolygonY1MixIn.y1 -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a first y-coordinate.<hr>

**[Returns]**

- `y1`: Int
  - A first y-coordinate.

## x2 property API

<!-- Docstring: apysc._display.polygon_x2_mixin.PolygonX2MixIn.x2 -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a second x-coordinate.<hr>

**[Returns]**

- `x2`: Int
  - A second x-coordinate.

## y2 property API

<!-- Docstring: apysc._display.polygon_y2_mixin.PolygonY2MixIn.y2 -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a second y-coordinate.<hr>

**[Returns]**

- `y2`: Int
  - A second y-coordinate.

## x3 property API

<!-- Docstring: apysc._display.polygon_x3_mixin.PolygonX3MixIn.x3 -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a third x-coordinate.<hr>

**[Returns]**

- `x3`: Int
  - A third x-coordinate.

## y3 property API

<!-- Docstring: apysc._display.polygon_y3_mixin.PolygonY3MixIn.y3 -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a third y-coordinate.<hr>

**[Returns]**

- `y3`: Int
  - A third y-coordinate.
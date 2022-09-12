# Path class

This page explains the `Path` class.

## What class is this?

The `Path` class creates a path vector graphics object.

## Basic usage

The `Path` class constructor requires the `path_data_list` argument.

The `path_data_list` argument is a list of each path setting, such as the `PathLineTo` or `PathBezier2D`.

The constructor also accepts each style's argument, such as the `fill_color` and `line_color`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
    ],
    line_color="0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_basic_usage/")
```

<iframe src="static/path_basic_usage/index.html" width="200" height="100"></iframe>

## PathMoveTo class setting

The `PathMoveTo` class is the class to set a new position on a path.

<iframe src="static/path_move_to_basic_usage/index.html" width="200" height="100"></iframe>

For more information, please see:

- [PathMoveTo class](path_move_to.md)

## PathLineTo class setting

The `PathLineTo` class is the class to set a new line from the current position on a path.

<iframe src="static/path_line_to_basic_usage/index.html" width="200" height="100"></iframe>

For more information, please see:

- [PathLineTo class](path_line_to.md)

## PathHorizontal class setting

The `PathHorizontal` class is the class to set a new horizontal line on a path.

<iframe src="static/path_horizontal_basic_usage/index.html" width="200" height="100"></iframe>

For more information, please see:

- [PathHorizontal class](path_horizontal.md)

## PathVertical class setting

The `PathVertical` class is the class to set a new vertical line on a path.

<iframe src="static/path_vertical_basic_usage/index.html" width="100" height="200"></iframe>

For more information, please see:

- [PathVertical class](path_vertical.md)

## PathClose class setting

The `PathClose` class is the class to close a path.

<iframe src="static/path_close_basic_usage/index.html" width="250" height="150"></iframe>

For more information, please see:

- [PathClose class](path_close.md)

## PathBezier2D class setting

The `PathBezier2D` class is the class to set a 2D bezier curve on a path.

<iframe src="static/path_bezier_2d_basic_usage_1/index.html" width="200" height="150"></iframe>

For more information, please see:

- [PathBezier2D class](path_bezier_2d.md)

## PathBezier2DContinual class setting

The `PathBezier2DContinual` class is the class to set a continual 2D bezier curve on a path.

<iframe src="static/path_bezier_2d_continual_basic_usage/index.html" width="400" height="200"></iframe>

For more information, please see:

- [PathBezier2DContinual class](path_bezier_2d_continual.md)

## PathBezier3D class setting

The `PathBezier3D` class is the class to set a 3D bezier curve on a path.

<iframe src="static/path_bezier_3d_basic_usage_1/index.html" width="250" height="270"></iframe>

For more information, please see:

- [PathBezier3D class](path_bezier_3d.md)

## PathBezier3DContinual class setting

The `PathBezier3DContinual` class is the class to set a continual 3D bezier curve on a path.

<iframe src="static/path_bezier_3d_continual_basic_usage_1/index.html" width="400" height="420"></iframe>

For more information, please see:

- [PathBezier3DContinual class](path_bezier_3d_continual.md)

## x property interface example

The `x` property updates or gets the instance's x-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=100, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=0, y=0),
        ap.PathLineTo(x=0, y=50),
        ap.PathLineTo(x=50, y=50),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=5,
)
path.x = ap.Int(50)

ap.save_overall_html(dest_dir_path="path_x/")
```

<iframe src="static/path_x/index.html" width="150" height="100"></iframe>

## y property interface example

The `y` property updates or gets the instance's y-coordinate:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=100, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=0, y=0),
        ap.PathLineTo(x=0, y=50),
        ap.PathLineTo(x=50, y=50),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=5,
)
path.y = ap.Int(50)

ap.save_overall_html(dest_dir_path="path_y/")
```

<iframe src="static/path_y/index.html" width="100" height="150"></iframe>

## fill_color property interface example

The `fill_color` property updates or gets the instance's fill color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
)
path.fill_color = ap.String("#0af")

ap.save_overall_html(dest_dir_path="path_fill_color/")
```

<iframe src="static/path_fill_color/index.html" width="150" height="150"></iframe>

## fill_alpha property interface example

The `fill_alpha` property updates or gets the instance's fill alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    fill_color="#0af",
)
path.fill_alpha = ap.Number(0.5)

ap.save_overall_html(dest_dir_path="path_fill_alpha/")
```

<iframe src="static/path_fill_alpha/index.html" width="150" height="150"></iframe>

## line_color property interface example

The `line_color` property updates or gets the instance's line color:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_thickness=5,
)
path.line_color = ap.String("#0af")

ap.save_overall_html(dest_dir_path="path_line_color/")
```

<iframe src="static/path_line_color/index.html" width="150" height="150"></iframe>

## line_alpha property interface example

The `line_alpha` property updates or gets the instance's line alpha (opacity):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=5,
)
path.line_alpha = ap.Number(0.5)

ap.save_overall_html(dest_dir_path="path_line_alpha/")
```

<iframe src="static/path_line_alpha/index.html" width="150" height="150"></iframe>

## line_thickness property interface example

The `line_thickness` property updates or gets the instance's line thickness (line width):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
)
path.line_thickness = ap.Int(10)

ap.save_overall_html(dest_dir_path="path_line_thickness/")
```

<iframe src="static/path_line_thickness/index.html" width="150" height="150"></iframe>

## line_dot_setting property interface example

The `line_dot_setting` property updates or gets the instance's line dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
path.line_dot_setting = ap.LineDotSetting(dot_size=3)

ap.save_overall_html(dest_dir_path="path_line_dot_setting/")
```

<iframe src="static/path_line_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_setting property interface example

The `line_dash_setting` property updates or gets the instance's line dash-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
path.line_dash_setting = ap.LineDashSetting(dash_size=7, space_size=2)

ap.save_overall_html(dest_dir_path="path_line_dash_setting/")
```

<iframe src="static/path_line_dash_setting/index.html" width="150" height="150"></iframe>

## line_round_dot_setting property interface example

The `line_round_dot_setting` property updates or gets the instance's line round dot-style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
)
path.line_round_dot_setting = ap.LineRoundDotSetting(round_size=5, space_size=4)

ap.save_overall_html(dest_dir_path="path_line_round_dot_setting/")
```

<iframe src="static/path_line_round_dot_setting/index.html" width="150" height="150"></iframe>

## line_dash_dot_setting property interface example

The `line_dash_dot_setting` property updates or gets the instance's dash-dotted line style setting:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
path.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=3,
    dash_size=6,
    space_size=3,
)

ap.save_overall_html(dest_dir_path="path_line_dash_dot_setting/")
```

<iframe src="static/path_line_dash_dot_setting/index.html" width="150" height="150"></iframe>

## rotation_around_center property interface example

The `rotation_around_center` property updates or gets the instance's rotation value (0 to 359) from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
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
    path.rotation_around_center += 1


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_rotation_around_center/")
```

<iframe src="static/path_rotation_around_center/index.html" width="150" height="150"></iframe>

## set_rotation_around_point and get_rotation_around_point methods interfaces example

The `set_rotation_around_point` method updates the instance's rotation value (0 to 359) from a specified point.

Similarly, the `get_rotation_around_point` method gets the instance's rotation value (0 to 359) from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
X: ap.Int = ap.Int(100)
Y: ap.Int = ap.Int(100)


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
    rotation: ap.Int = path.get_rotation_around_point(x=X, y=Y) + 1
    path.set_rotation_around_point(rotation=rotation, x=X, y=Y)


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_rotation_around_point/")
```

<iframe src="static/path_rotation_around_point/index.html" width="150" height="150"></iframe>

## scale_x_from_center property interface example

The `scale_x_from_center` property updates or gets the instance's scale-x from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)


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
    scale: ap.Number = path.scale_x_from_center
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    path.scale_x_from_center += direction * 0.01


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_x_from_center/")
```

<iframe src="static/path_scale_x_from_center/index.html" width="150" height="150"></iframe>

## scale_y_from_center property interface example

The `scale_y_from_center` property updates or gets the instance's scale-y from the center point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)


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
    scale: ap.Number = path.scale_y_from_center
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    path.scale_y_from_center += direction * 0.01


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_y_from_center/")
```

<iframe src="static/path_scale_y_from_center/index.html" width="150" height="150"></iframe>

## set_scale_x_from_point and get_scale_x_from_point methods interfaces example

The `set_scale_x_from_point` method updates the instance's scale-x from a specified point.

Similarly, the `get_scale_x_from_point` method gets the instance's scale-x from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)
X: ap.Int = ap.Int(100)


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
    scale: ap.Number = path.get_scale_x_from_point(x=X)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    scale += direction * 0.005
    path.set_scale_x_from_point(scale_x=scale, x=X)


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_x_from_point/")
```

<iframe src="static/path_scale_x_from_point/index.html" width="150" height="150"></iframe>

## set_scale_y_from_point and get_scale_y_from_point methods interfaces example

The `set_scale_y_from_point` method updates the instance's scale-y from a specified point.

Similarly, the `get_scale_y_from_point` method gets the instance's scale-y from a specified point:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
    ],
    line_color="#0af",
    line_thickness=3,
)
direction: ap.Int = ap.Int(1)
Y: ap.Int = ap.Int(100)


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
    scale: ap.Number = path.get_scale_y_from_point(y=Y)
    with ap.If(scale <= 0.001):
        direction.value = 1
    with ap.If(scale >= 2):
        direction.value = -1
    scale += direction * 0.005
    path.set_scale_y_from_point(scale_y=scale, y=Y)


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_scale_y_from_point/")
```

<iframe src="static/path_scale_y_from_point/index.html" width="150" height="150"></iframe>

## flip_x property interface example

The `flip_x` property updates or gets the instance's flip-x (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
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
    path.flip_x = path.flip_x.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="path_flip_x/")
```

<iframe src="static/path_flip_x/index.html" width="150" height="150"></iframe>

## flip_y property interface example

The `flip_y` property updates or gets the instance's flip-y (reflecting state) boolean value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
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
    path.flip_y = path.flip_y.not_


ap.Timer(handler=on_timer, delay=1000).start()
ap.save_overall_html(dest_dir_path="path_flip_y/")
```

<iframe src="static/path_flip_y/index.html" width="150" height="150"></iframe>

## skew_x property interface example

The `skew_x` property updates or gets the instance's skew-x (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
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
    path.skew_x += 1


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_skew_x/")
```

<iframe src="static/path_skew_x/index.html" width="150" height="150"></iframe>

## skew_y property interface example

The `skew_y` property updates or gets the instance's skew-y (distortion) value:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=150, stage_height=150, stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=50, y=100),
        ap.PathLineTo(x=100, y=100),
        ap.PathClose(),
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
    path.skew_y += 1


ap.Timer(handler=on_timer, delay=ap.FPS.FPS_60).start()
ap.save_overall_html(dest_dir_path="path_skew_y/")
```

<iframe src="static/path_skew_y/index.html" width="150" height="150"></iframe>

## Path class constructor API

<!-- Docstring: apysc._display.path.Path.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, path_data_list: List[apysc._geom.path_data_base.PathDataBase], fill_color: Union[str, apysc._type.string.String] = '', fill_alpha: Union[float, apysc._type.number.Number] = 1.0, line_color: Union[str, apysc._type.string.String] = '', line_alpha: Union[float, apysc._type.number.Number] = 1.0, line_thickness: Union[int, apysc._type.int.Int] = 1, line_cap: Union[apysc._type.string.String, apysc._display.line_caps.LineCaps, NoneType] = None, line_joints: Union[apysc._type.string.String, apysc._display.line_joints.LineJoints, NoneType] = None, line_dot_setting: Union[apysc._display.line_dot_setting.LineDotSetting, NoneType] = None, line_dash_setting: Union[apysc._display.line_dash_setting.LineDashSetting, NoneType] = None, line_round_dot_setting: Union[apysc._display.line_round_dot_setting.LineRoundDotSetting, NoneType] = None, line_dash_dot_setting: Union[apysc._display.line_dash_dot_setting.LineDashDotSetting, NoneType] = None, parent: Union[apysc._display.child_interface.ChildInterface, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]** Create a path vector graphic.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.
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
- `parent`: ChildInterface or None, default None
  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> path: ap.Path = ap.Path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...     ],
...     line_color="#ffffff",
...     line_thickness=3,
... )
>>> path.line_color
String('#ffffff')

>>> path.line_thickness
Int(3)
```

<hr>

**[References]**

- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathMoveTo class](https://simon-ritchie.github.io/apysc/en/path_move_to.html)
- [PathLineTo class](https://simon-ritchie.github.io/apysc/en/path_line_to.html)
- [PathHorizontal class](https://simon-ritchie.github.io/apysc/en/path_horizontal.html)
- [PathVertical class](https://simon-ritchie.github.io/apysc/en/path_vertical.html)
- [PathClose class](https://simon-ritchie.github.io/apysc/en/path_close.html)
- [PathBezier2D class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html)
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)
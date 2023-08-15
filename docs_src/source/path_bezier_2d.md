# PathBezier2D class

This page explains the `PathBezier2D` class.

## What class is this?

The `PathBezier2D` class is the class to set a 2D bezier curve on a path.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathBezier2D` class constructor requires the `control_x`, `control_y`, `dest_x`, and `dest_y` arguments.

The `control_x` and `control_y` are the coordinates to determine the control point of the bezier curve.

The `dest_x` and `dest_y` are the bezier curve's destination coordinates.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=150,
    stage_elem_id="stage",
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=100,
            control_y=25,
            dest_x=150,
            dest_y=100,
        ),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_1/")
```

<iframe src="static/path_bezier_2d_basic_usage_1/index.html" width="200" height="150"></iframe>

In the following example, the magenta circle shows the control point.

Similarly, the cyan circle shows the destination point.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=150,
    stage_elem_id="stage",
)

CONTROL_X: float = 100
CONTROL_Y: float = 25
DEST_X: float = 150
DEST_Y: float = 100
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=CONTROL_X,
            control_y=CONTROL_Y,
            dest_x=DEST_X,
            dest_y=DEST_Y,
        ),
    ],
    line_color=ap.Color("#fff"),
    line_thickness=5,
)

RADIUS: int = 5
magenta_circle: ap.Circle = ap.Circle(
    x=CONTROL_X,
    y=CONTROL_Y,
    radius=RADIUS,
    fill_color=ap.Color("#f0a"),
)
cyan_circle: ap.Circle = ap.Circle(
    x=DEST_X,
    y=DEST_Y,
    radius=RADIUS,
    fill_color=ap.Color("#0af"),
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_basic_usage_2/")
```

<iframe src="static/path_bezier_2d_basic_usage_2/index.html" width="200" height="150"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

A criteria point is a starting point, not a control point.

The following example sets the relative setting and draws the bezier curve.

Since it uses the `relative` setting, the `control_y` parameter becomes the minus value, and the `dest_y` becomes zero:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=200,
    stage_height=150,
    stage_elem_id="stage",
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=100),
        ap.PathBezier2D(
            control_x=50, control_y=-75, dest_x=100, dest_y=0, relative=True
        ),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_2d_relative/")
```

<iframe src="static/path_bezier_2d_relative/index.html" width="200" height="150"></iframe>

## PathBezier2D class constructor API

<!-- Docstring: apysc._geom.path_bezier_2d.PathBezier2D.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, control_x: Union[float, apysc._type.number.Number], control_y: Union[float, apysc._type.number.Number], dest_x: Union[float, apysc._type.number.Number], dest_y: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Path data class for the SVG's `2D bezier curve` (Q).<hr>

**[Parameters]**

- `control_x`: float or Number
  - X-coordinate of the bezier's control point.
- `control_y`: float or Number
  - Y-coordinate of the bezier's control point.
- `dest_x`: float or Number
  - X-coordinate of the destination point.
- `dest_y`: float or Number
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathBezier2DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html)
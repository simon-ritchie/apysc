# PathBezier3D class

This page explains the `PathBezier3D` class.

## What class is this?

The `PathBezier3D` class is the class to set a 3D bezier curve on a path.

This class has two control points (as a comparison, the 2D bezier class has one control point).

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathBezier3D` class constructor requires the `control_x1`, `control_y1`, `control_x2`, `control_y2`, `dest_x`, and `dest_y` arguments.

The `control_x1` and `control_y1` are the coordinates to determine the first control point of the bezier curve.

Similarly, the `control_x2` and `control_y2` are the coordinates to determine the second control point of the bezier curve.

The `dest_x` and `dest_y` are the bezier curve's destination coordinates.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=200),
        ap.PathBezier3D(
            control_x1=50,
            control_y1=25,
            control_x2=200,
            control_y2=25,
            dest_x=200,
            dest_y=200,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_1/")
```

<iframe src="static/path_bezier_3d_basic_usage_1/index.html" width="250" height="270"></iframe>

In the following example, the cyan circle shows the first control point of the bezier curve.

The magenta circle shows the second control point of the bezier curve.

And also, the yellow circle shows the destination point of the bezier curve.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"
)

CONTROL_X1: int = 50
CONTROL_Y1: int = 25
CONTROL_X2: int = 200
CONTROL_Y2: int = 25
DEST_X: int = 200
DEST_Y: int = 200

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=200),
        ap.PathBezier3D(
            control_x1=CONTROL_X1,
            control_y1=CONTROL_Y1,
            control_x2=CONTROL_X2,
            control_y2=CONTROL_Y2,
            dest_x=DEST_X,
            dest_y=DEST_Y,
        ),
    ],
    line_color="#fff",
    line_thickness=5,
)

RADIUS: int = 10
cyan_circle: ap.Circle = ap.Circle(
    x=CONTROL_X1,
    y=CONTROL_Y1,
    radius=RADIUS,
    fill_color="#0af",
)

magenta_circle: ap.Circle = ap.Circle(
    x=CONTROL_X2,
    y=CONTROL_Y2,
    radius=RADIUS,
    fill_color="#f0a",
)

yellow_circle: ap.Circle = ap.Circle(
    x=DEST_X,
    y=DEST_Y,
    radius=RADIUS,
    fill_color="#ff0",
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_basic_usage_2/")
```

<iframe src="static/path_bezier_3d_basic_usage_2/index.html" width="250" height="270"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

A criteria point is a starting point, neither a first control point nor a second control point.

The following example sets the relative setting and draws the bezier curve.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=250, stage_height=270, stage_elem_id="stage"
)

path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=200),
        ap.PathBezier3D(
            control_x1=0,
            control_y1=-175,
            control_x2=150,
            control_y2=-175,
            dest_x=150,
            dest_y=0,
            relative=True,
        ),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_relative/")
```

<iframe src="static/path_bezier_3d_relative/index.html" width="250" height="270"></iframe>

## PathBezier3D class constructor API

<!-- Docstring: apysc._geom.path_bezier_3d.PathBezier3D.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, control_x1: Union[int, apysc._type.int.Int], control_y1: Union[int, apysc._type.int.Int], control_x2: Union[int, apysc._type.int.Int], control_y2: Union[int, apysc._type.int.Int], dest_x: Union[int, apysc._type.int.Int], dest_y: Union[int, apysc._type.int.Int], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Path data class for the SVG's `3D bezier curve` (C).<hr>

**[Parameters]**

- `control_x1`: Int or int
  - X-coordinate of the bezier's first control point.
- `control_y1`: Int or int
  - Y-coordinate of the bezier's first control point.
- `control_x2`: Int or int
  - X-coordinate of the bezier's second control point.
- `control_y2`: Int or int
  - Y-coordinate of the bezier's second control point.
- `dest_x`: Int or int
  - X-coordinate of the destination point.
- `dest_y`: Int or int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0,
...             control_y1=0,
...             control_x2=50,
...             control_y2=0,
...             dest_x=50,
...             dest_y=50,
...         ),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100, dest_x=100, dest_y=50
...         ),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)
- [PathBezier3DContinual class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html)
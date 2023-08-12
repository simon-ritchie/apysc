# PathBezier3DContinual class

This page explains the `PathBezier3DContinual` class.

## What class is this?

The `PathBezier3DContinual` class is the class to set a continual 3D bezier curve on a path.

This setting draws a smooth curve by using a line-symmetric control point.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathBezier3DContinual` class constructor requires the `control_x`, `control_y`, `dest_x`, and `dest_y` arguments.

The `control_x` and `control_y` are the second control point of a bezier curve.

A line-symmetric control point of a bezier curve's second control point becomes the first control point of the `PathBezier3DContinual` setting.

So there are no arguments to set the first control point in the `PathBezier3DContinual` constructor.

The `dest_x` and `dest_y` are the destination point of a bezier curve.

The `PathBezier3DContinual` class has the restriction, and you can use this class only after the `PathBezier3D` or `PathBezier3DContinual`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=400,
    stage_height=420,
    stage_elem_id="stage",
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
        ap.PathBezier3DContinual(
            control_x=350,
            control_y=375,
            dest_x=350,
            dest_y=200,
        ),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_1/")
```

<iframe src="static/path_bezier_3d_continual_basic_usage_1/index.html" width="400" height="420"></iframe>

In the following example, the cyan circle shows the control point (`control_x` and `control_y`), and the magenta circle shows the destination point (`dest_x` and `dest_y`):

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=400,
    stage_height=420,
    stage_elem_id="stage",
)

CONTROL_X: float = 350
CONTROL_Y: float = 375
DEST_X: float = 350
DEST_Y: float = 200

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
        ap.PathBezier3DContinual(
            control_x=CONTROL_X,
            control_y=CONTROL_Y,
            dest_x=DEST_X,
            dest_y=DEST_Y,
        ),
    ],
    line_color=ap.Color("#fff"),
    line_thickness=5,
)

RADIUS: int = 10

cyan_circle: ap.Circle = ap.Circle(
    x=CONTROL_X,
    y=CONTROL_Y,
    radius=RADIUS,
    fill_color=ap.Color("#0af"),
)

magenta_circle: ap.Circle = ap.Circle(
    x=DEST_X,
    y=DEST_Y,
    radius=RADIUS,
    fill_color=ap.Color("#f0a"),
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_continual_basic_usage_2/")
```

<iframe src="static/path_bezier_3d_continual_basic_usage_2/index.html" width="400" height="420"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

A criteria point is a starting point, not a control point.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=400,
    stage_height=420,
    stage_elem_id="stage",
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
        ap.PathBezier3DContinual(
            control_x=150,
            control_y=175,
            dest_x=150,
            dest_y=0,
            relative=True,
        ),
    ],
    line_color=ap.Color("#0af"),
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_bezier_3d_continual_relative/")
```

<iframe src="static/path_bezier_3d_continual_relative/index.html" width="400" height="420"></iframe>

## PathBezier3DContinual class constructor API

<!-- Docstring: apysc._geom.path_bezier_3d_continual.PathBezier3DContinual.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, control_x: Union[float, apysc._type.number.Number], control_y: Union[float, apysc._type.number.Number], dest_x: Union[float, apysc._type.number.Number], dest_y: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Path data class for SVG's `continual 3D bezier curve` (S).<hr>

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
- [PathBezier3D class](https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html)